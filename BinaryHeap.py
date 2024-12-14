from random import randint

def swap(a,i,j):
    piv = a[i]
    a[i] = a[j]
    a[j] = piv

class BinaryHeap:
    def comparatorMinHeap(self,a,b):
        return True if a <= b else False
    def comparatorMaxHeap(self,a,b):
        return True if a >= b else False

    def __init__(self, w=1, min=True):
        self.h = [None for i in range(w+1)]
        self.n = 0
        if min: self.invariantComparator = self.comparatorMinHeap
        else: self.invariantComparator = self.comparatorMaxHeap
    
    def top(self):
        return self.h[1]
    
    def insert(self,e):
        self.n += 1
        self.h.append(None)
        self.h[self.n] = e
        self.siftUp(self.n)

    def siftUp(self,j):
        if j == 1 or self.invariantComparator(self.h[int(j/2)],self.h[j]): return
        swap(self.h, j, int(j/2))
        self.siftUp(int(j/2))

    def delMin(self):
        assert self.n > 0
        result = self.h[1]
        self.h[1] = self.h[self.n]
        self.n -= 1
        self.siftDown(1)
        return result

    def siftDown(self,j):
        if 2*j <= self.n:
            if 2*j + 1 > self.n or self.invariantComparator(self.h[2*j],self.h[2*j+1]): m = 2*j 
            else: m = 2*j+1
            if not self.invariantComparator(self.h[j], self.h[m]):
                swap(self.h,j,m)
                self.siftDown(m)

    def buildHeapBackwards(self,a):
        self.h = a
        self.n = len(a)-1
        r = range(int(self.n/2),0,-1)
        for j in r:
            self.siftDown(j)

def heapSort(a):
    h = BinaryHeap(len(a),False)
    h.buildHeapBackwards([None] + a)
    for i in range(len(a),1,-1):
        swap(h.h,1,i)
        h.n -= 1
        h.siftDown(1)
    return h.h

array = [randint(0,20) for i in range(50)]
print(heapSort(array))