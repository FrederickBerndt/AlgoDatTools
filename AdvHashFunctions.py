import numpy as np

def universal_hashfk(a, b, m):
    list_a = []
    list_b = []
    while a != 0:
        list_a.append(a%m)
        a = a//m
    while b != 0:
        list_b.append(b%m)
        b = b//m
    while len(list_a)>len(list_b): list_b = list_b + [0]
    while len(list_b)>len(list_a): list_a = list_a + [0]
    vec_a = np.array(list_a)
    vec_b = np.array(list_b)
    dot_ab = np.dot(vec_a, vec_b)
    return dot_ab % m

def find_perf_hash(M, n, m):
    a = 0
    notperfect = True
    while notperfect:
        a += 1g

        ##TestIfPerfect
        probeSet = set()
        notperfect = False
        for e in M:
            key = universal_hashfk(e,a,m)
            if key in probeSet:
                notperfect = True
                break
            else:
                probeSet.add(key)
    return a
