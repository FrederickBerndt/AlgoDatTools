from random import randint, random
from math import ceil

def swap(a,i,j):
    piv = a[i]
    a[i] = a[j]
    a[j] = piv

def insertionSort(a):
    """
        Sortierung in-place, stabil aufsteigend 
    """
    if len(a) < 2: return a
    for i in range(1,len(a)):
        j = i
        while a[j-1] > a[j] and j != 0:
            swap(a,j-1,j)
            j -= 1

def selectionSort(a):
    """
        Sortierung in-place
    """
    for i in range(len(a)):
        m = i
        for j in range(i + 1, len(a)):
            if a[j] < a[m]: m = j
        if m != i: swap(a,i,m)

def mergeSort(a):
    if len(a) <= 1: return a
    else:
        split = int(len(a)/2)
        return merge(mergeSort(a[0:split]), mergeSort(a[split:len(a)]))

def merge(a,b):
    c = []
    while len(a) != 0 and len(b) != 0:
        if a[0] < b[0]:
            c.append(a.pop(0))
        else:
            c.append(b.pop(0))
    if len(a) != 0: c += a
    if len(b) != 0: c += b
    return c

def qSort(a,l,r):
    if r-l > 0:
        p = choosePivotPos(a,l,r)
        (i,j,p) = partition(a,l,r,p)
        qSort(a,l,j-1)
        qSort(a,j+1,r)

def partition(a,l,r,p):
    i = l - 1
    j = r + 1
    while True:
        i += 1
        while a[i] < p: i += 1
        j -= 1
        while a[j] > p: j -= 1
        if i >= j: return j
        swap(a,i,j)

def hoarePartition(a,i,j,p):
    assert(i<=p<=j)
    pivot = a[p]
    while True:
        while a[i] < pivot: i += 1
        while a[j] > pivot: j -= 1
        if i <= j: 
            swap(a,i,j)
            i += 1
            j -= 1
        if i > j: break
    return (i,j,pivot)    

def qSelect(a,l,r,k):
    p = mediansOfMedians(a,l,r)
    j = partition(a,l,r,p)
    if k == j: return a[j]
    elif k < j: return qSelect(a, l, j, k)
    else: return qSelect(a, j, r, k)

def choosePivotPos(a,l,r):
    #return l if l-r <= 2 else int((r + l) / 2)
    return randint(l,r)

def mediansOfMedians(a,l,r):
    medians = []
    i = -1
    while i + 5 < r-l:
        medians.append(mediansOf5(a,i+1,i+5))
        i += 5
    rest_m = mediansOf5(a,i+1,r)
    if rest_m is not None: medians.append(rest_m) 
    return qSelect(medians, 0, len(medians)-1, ceil(int(len(medians)/5)/2)) if len(medians) != 1 else medians[0]

def mediansOf5(a,l,r):
    if r-l != 0:
        insertionSort(a[l:r+1])
        return a[int((l+r)/2)]

def keyLSD(x,i):
    return (x // (10**i)) % 10

def lsdRadixSort(a,d):
    for i in range(0,d):
        b = [[],[],[],[],[],[],[],[],[],[]]
        for e in a: 
            b[keyLSD(e,i)].append(e)
        a = [item for sub in b for item in sub]
    return a

def uniformSort(a):
    b = [[] for i in range(len(a))]
    for e in a:
        b[int(e*len(a))].append(e)
    for i in range(0,len(a)):
        insertionSort(b[i])
    return [e for b_i in b for e in b_i]


array = [random() for i in range(10)]
print(qSort(array, 0, 10))
print(array)
#print(uniformSort(array))

