from random import randint
from math import ceil
from BinarySearchTree import BinarySearchTree

class KSPProcessor:
    def __init__(self,e):
        self.n = 0
        self.e = e
        self.tree = BinarySearchTree()

    def nextValue(self,x):
        (parent, e) = self.tree.locateParentByKey(x)
        if e is not None and e.data[0] == x:
            e.data[1] += 1
            self.n += 1
        else:
            self.n += 1
            self.tree.insert([x,1])
            if self.tree.dll.size > ceil(2/self.e):
                currentElement = self.tree.dll.dummy.next
                while True:
                    currentElement.data[1] -=1
                    if currentElement.data[1] == 0:
                        self.tree.remove(currentElement.data[0])
                    if currentElement.next is self.tree.dll.dummy: break
                    else: currentElement = currentElement.next

    def evaluate(self):
        heavyHitter = []
        currentElement = self.tree.dll.dummy.next
        while currentElement is not self.tree.dll.dummy:
            if currentElement.data[1] >= self.e*self.n/2:
                heavyHitter.append(currentElement.data[0])
            currentElement = currentElement.next
        return heavyHitter

a = [1,2,1,3,4,1,1,3,1,5,1,3,1,3,1]
KSPP = KSPProcessor(1/2)
for x in a: KSPP.nextValue(x)
print(KSPP.evaluate())
