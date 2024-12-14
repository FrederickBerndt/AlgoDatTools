from random import randint
class Element:
    def __init__(self,x,p=None,n=None):
        self.data = x
        self.previous = p
        self.next = n

class DoublyLinkedList:
    def __init__(self,a=[]):
        self.dummy = Element([float("inf"),None])
        self.dummy.next = self.dummy
        self.dummy.previous = self.dummy
        self.size = 0
        self.isEmpty = True
        for e in a: self.insertAfter(e,self.last)

    def insertAfter(self,x,handle):
        newElement = Element(x,handle,handle.next)
        handle.next.previous = newElement
        handle.next = newElement
        self.size += 1

    def removeElement(self,e):
        e.previous.next = e.next
        e.next.previous = e.previous
        self.size -= 1

class BinarySearchTree:
    class Splitter:
        def __init__(self,k,p=None,l=None,r=None):
            self.key = k
            self.parent = p # can be of Type None or Splitter 
            self.left = l # can be of Type None, Splitter or ListElemet
            self.right = r # can be of Type None, splitter or ListElement

    def __init__(self, keyValuePairsList=[]):
        self.dll = DoublyLinkedList()
        self.root = None
        for keyValuePair in keyValuePairsList: self.insert(keyValuePair)

    def height(self,node):
        if type(node) == Element: return 0
        if node.left is not None or node.rights is not None: return max(self.height(node.left),self.height(node.right)) + 1

    def hasKey(self,key):
        (parent, e) = self.locateParentByKey(key)
        return e.data[0] == key

    def insert(self,keyValuePair):
        if self.root is None:
            assert self.dll.dummy is self.dll.dummy.next
            self.dll.insertAfter(keyValuePair,self.dll.dummy)
            self.root = self.Splitter(keyValuePair[0],None,self.dll.dummy.next,self.dll.dummy)
        else:
            (eDashParent, eDash) = self.locateParentByKey(keyValuePair[0])
            if eDash.data ==  keyValuePair[0]: 
                eDash.data = keyValuePair
            else:
                self.dll.insertAfter(keyValuePair,eDash.previous)
                if eDash is eDashParent.left: eDashParent.left = self.Splitter(keyValuePair[0],eDashParent,eDash.previous,eDash)
                elif eDash is eDashParent.right: eDashParent.right = self.Splitter(keyValuePair[0],eDashParent,eDash.previous,eDash)

    def locateParentByKey(self,key):
        e = self.root
        parent = None
        while True:
            if type(e) == self.Splitter: 
                parent = e
                if key > e.key: e = e.right
                else: e = e.left
            else: break
        if parent is not None and key > e.data[0]: return self.locateParentByKey(e.next.data[0])
        else: return (parent,e)

    def remove(self,key):
        (eParent, e) = self.locateParentByKey(key)
        kDash = eParent.key
        k = e.data[0]
        if e.data[0] == key:
            if e is eParent.left:
                if eParent is self.root:
                    if self.Splitter == type(eParent.right):
                        self.root = eParent.right
                else:
                    parentOfeParent = eParent.parent
                    if eParent is parentOfeParent.left: 
                        parentOfeParent.left = eParent.right
                        parentOfeParent.left.parent = parentOfeParent
                    elif eParent is parentOfeParent.right: 
                        parentOfeParent.right = eParent.right
                        parentOfeParent.right.parent = parentOfeParent
            elif e is eParent.right:
                if eParent is self.root:
                    if self.Splitter == type(eParent.left):
                        self.root = eParent.left
                else:
                    parentOfeParent = eParent.parent
                    if eParent is parentOfeParent.left: 
                        parentOfeParent.left = eParent.left
                        parentOfeParent.left.parent = parentOfeParent
                    elif eParent is parentOfeParent.right: 
                        parentOfeParent.right = eParent.left
                        parentOfeParent.right.parent = parentOfeParent
                    currentSplitter = parentOfeParent
                    while currentSplitter is not self.root:
                        if currentSplitter.key == k: 
                            currentSplitter.key = kDash
                            break
                        currentSplitter = currentSplitter.parent
            self.dll.removeElement(e)

#a = [[3,3],[1,1],[5,5],[0,0],[2,2],[4,4],[6,6]]
#a = [randint(0,1000) for i in range(100)]
#BST = BinarySearchTree(a)
"""
    3
  1   5
 0 2 4 6
0123456
heights = []
for i in range(1000):
    a = [randint(0,100) for i in range(1000)]
    BST = BinarySearchTree(a)
    heights.append(BST.height(BST.root))
"""
#print(sum(heights)/1000)
#print(BST.hasKey(7))
#print("Hie")