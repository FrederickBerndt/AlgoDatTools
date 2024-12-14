import numpy as np

def n_n_sum(a_array,b_array):
    sum = np.array([0]*(len(a_array)+1))
    if len(a_array) > len(b_array): b_array = np.pad(b_array, (len(a_array) - len(b_array), 0))
    else: a_array = np.pad(a_array, (len(b_array) - len(a_array), 0))
    n = len(a_array)
    for i in range(n):
        sum_ = a_array[n-i-1]+b_array[n-i-1]
        sum[n-i] += sum_%10
        sum[n-i-1] = sum_//10
    return sum

#print(n_n_sum([9,1,1], [9,2,3]))

def n_1_product(a_array, b):
    c = 0
    n = len(a_array)
    p = np.array([0]*(n+1))
    for i in range(n):
        p_ = a_array[n-i-1]*b
        a = p_%10
        c = p_//10
        p[n-i] += a
        p[n-i-1] = c
    return p

def schulmethode(a,b):
    a_array = np.array(list(str(a)), dtype=int)
    b_array = np.array(list(str(b)), dtype=int)
    if len(a_array) > len(b_array): b_array = np.pad(b_array, (len(a_array) - len(b_array), 0))
    else: a_array = np.pad(a_array, (len(b_array) - len(a_array), 0))
    n = len(a_array)
    p = np.array([0]*2*n)
    for j in range(n):
        p_ = n_1_product(a_array, b_array[n-j-1])
        f = p[2*n-1-j-n:2*n-j]
        sum = n_n_sum(p_, f)
        for i in range(n+1):
            p[2*n-j-i-1] = sum[n-i+1]
    return p

def vSchulmethode(a,b):
    a_array = np.array(list(str(a)), dtype=int)
    b_array = np.array(list(str(b)), dtype=int)
    if len(a_array) > len(b_array): b_array = np.pad(b_array, (len(a_array) - len(b_array), 0))
    else: a_array = np.pad(a_array, (len(b_array) - len(a_array), 0))
    n = len(a_array)
    return recSchulmethode(a_array, b_array)

def recSchulmethode(a_array, b_array):
    n = len(a_array)
    if len(a_array) > 1 and len(b_array) > 1:
        k = int(n/2)
        a_0 = a_array[:k]
        a_1 = a_array[k:]
        b_0 = b_array[:k]
        b_1 = b_array[k:]
        p1 = np.concatenate((recSchulmethode(a_1,b_1),[0]*2*k))
        p2 = np.concatenate((n_n_sum(recSchulmethode(a_1,b_0), recSchulmethode(a_0,b_1)),[0]*k))
        p3 = recSchulmethode(a_0,b_0)
        p1[len(p1)-len(p2):] += p2
        p1[len(p1)-len(p3):] += p3
        return p1
    elif len(a_array) < 1 or len(b_array) < 1:
        return [0]
    else:
        return a_array*b_array

print(vSchulmethode(11,2))