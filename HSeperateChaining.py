import math
from random import randint
import numpy as np

def c_uni_HashF(a,b,m):
    list_a = []
    list_b = []
    while a != 0:
        list_a.append(a%m)
        a = a//m
    while b != 0:
        list_b.append(b%m)
        b = b//m
    while len(list_a) > len(list_b): list_b = list_b + [0]
    while len(list_b) > len(list_a): list_a = list_a + [0]
    vec_a = np.array(list_a)
    vec_b = np.array(list_b)
    dot_ab = np.dot(vec_a, vec_b)
    return int(dot_ab % m)

def simple_mod_HashF(a,x,m):
    return x % m

def next_prime_to(x):
    for p in range(x+1,2*x):
        is_prime = True
        for n in range(2, int(math.sqrt(p))+1):
            if p % n == 0: 
                is_prime = False
                break
        if is_prime: return p

class ListElement:
    def __init__(self,d,n=None):
        self.data = d
        self.next = n

class hashtable:
    def __init__(self,f=simple_mod_HashF):
        self.m = 2
        self.n = 0
        self.hf = f
        self._table = []
        for i in range(self.m): 
            a = ListElement(None)
            a.next = a
            self._table.append(a)
        self.a = 7 #randint(5, self.m*self.m+10)
        self.alpha = 1/2
        self.betha = 1/4
    
    def insert_from(self, key_value_pairs):
        for e in key_value_pairs:
            if e != None: self.insert(e)

    def insert(self, x):
        assert len(x) == 2
        inserted = False 
        hashvalue = self.hf(self.a, x[0], self.m)
        currrentElement = self._table[hashvalue].next
        while currrentElement is not self._table[hashvalue] and not inserted:
            if currrentElement.data[0] == x[0]:
                currrentElement.data = x
                inserted = True
            currrentElement = currrentElement.next
        if not inserted:
            newElement = ListElement(x,self._table[hashvalue])
            currrentElement.next = newElement
            self.n += 1
        if self.n/self.m >= self.alpha:
            self.m = next_prime_to(self.m*int((1/self.alpha)))
            self.n = 0
            oldTable = self._table
            self._table = []
            for i in range(self.m):
                a = ListElement(None)
                a.next = a
                self._table.append(a)
            for ChainRoot in oldTable:
                currrentElement = ChainRoot.next
                while currrentElement is not ChainRoot:
                    self.insert(currrentElement.data)
                    currrentElement = currrentElement.next

    def remove(self, key):
        if key is None: return
        hashvalue = self.hf(self.a, key, self.m)
        previousElement = self._table[hashvalue]
        currentElement = previousElement.next
        while currentElement is not self._table[hashvalue]:
            if currentElement.data[0] == key:
                previousElement.next = currentElement.next
                self.n -= 1
                break
            previousElement = currentElement
            currentElement = currentElement.next
        if self.n/self.m < self.betha:
            self.m = next_prime_to(int(self.m*self.betha)*2)
            self.n = 0
            oldTable = self._table
            self._table = []
            for i in range(self.m):
                a = ListElement(None)
                a.next = a
                self._table.append(a)
            for ChainRoot in oldTable:
                currrentElement = ChainRoot.next
                while currrentElement is not ChainRoot:
                    self.insert(currrentElement.data)
                    currrentElement = currrentElement.next

    def find(self, key):
        hashvalue = self.hf(self.a, key, self.m)
        self._table[hashvalue].data = [key,0]
        currentElement = self._table[hashvalue].next
        while currentElement.data[0] != key:
            currentElement = currentElement.next
        self._table[hashvalue].data = None
        if currentElement is self._table[hashvalue]: return None
        else: return currentElement.data[1]

T = hashtable()
key_value_pairs = [[randint(0,100),randint(0,100)] for i in range(0,100)] + [[1,12]]
T.insert_from(key_value_pairs)
print(T._table)
T.remove(1)
print(T.find(1))