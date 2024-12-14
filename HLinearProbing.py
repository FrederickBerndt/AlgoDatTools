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

class hashtable:
    def __init__(self,f=simple_mod_HashF):
        self.m = 2
        self.n = 0
        self.hf = f
        self._table = [None]*self.m
        self.a = 7 #randint(5, self.m*self.m+10)
        self.alpha = 9/10
        self.betha = 1/4
    
    def insert_from(self, key_value_pairs):
        for e in key_value_pairs:
            if e != None: self.insert(e)

    def insert(self, x):
        inserted = False 
        hashvalue = self.hf(self.a, x[0], self.m)
        index = hashvalue
        while not inserted:
            if self._table[index] is not None:
                if self._table[index][0] == x[0]:
                    self._table[index][1] = x[1]
                    inserted = True
                index = (index+1) % self.m
            else:
                self._table[index] = x
                inserted = True
        self.n += 1
        if self.n/self.m >= self.alpha:
            self.m = next_prime_to(self.m*int((1/self.alpha)))
            key_value_pairs = self._table
            self._table = [None]*self.m
            self.n = 0
            self.insert_from(key_value_pairs)

    def remove(self, x):
        if x is None: return
        index = self.hf(self.a, x[0], self.m)
        self._table[index] = None
        j = index + 1
        k = index
        l = index
        while j != k:
            if self._table[j] is None: break
            else:
                f = self._table[j]
                h = self.hf(self.a, f[0], self.m)
                if l <= h <= index:
                    self._table[index] = f
                    self._table[j] = None
                    index = j
                j = j + 1
                if j == self.m: 
                    j = 0
                    l = 0
        self.n -= 1
        if self.n/self.m < self.betha:
            self.m = next_prime_to(int(self.m*self.betha)*2)
            key_value_pairs = self._table
            self._table = [None]*self.m
            self.n = 0
            self.insert_from(key_value_pairs)

    def find(self, key):
        index = self.hf(self.a, key, self.m)
        j = 0
        while j != self.m:
            if self._table[index+j] is None: return None
            elif self._table[index+j][0] == key:
                return self._table[index+j][1]
            else: j += 1
        return None
             

T = hashtable()
key_value_pairs = [[randint(0,100),randint(0,100)] for i in range(0,100)]
T.insert_from(key_value_pairs)
print(T._table)
