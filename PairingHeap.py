class Element:
    def __init__(self,x,a=None,b=None,c=None):
        self.data = x
        self.parent = a
        self.leftChild = b
        self.rightSibling = c

class PairingHeap:
    def __init__(self,r=[]): # in O(|r|)
        self.minPtr = None
        self.roots = []
        for x in r:
            self.insert(x)

    def insert(self,x): # in O(1)
        self.roots.append(Element(x,None,None,None))
        if self.min() >= x: self.minPtr = self.roots[len(self.roots)-1]
        if len(self.roots) >= 2: self.combine(self.roots[0],self.roots[1])
 
    def min(self): # in O(1)
        if self.minPtr is not None: return self.minPtr.data
        else: return float("inf")

    def combine(self,rootA,rootB): # in O(1)
        if rootA.data < rootB.data: 
            smallerRoot = rootA
            biggerRoot = rootB
        else: 
            smallerRoot = rootB
            biggerRoot = rootA
        biggerRoot.parent = smallerRoot
        biggerRoot.rightSibling = smallerRoot.leftChild
        smallerRoot.leftChild = biggerRoot
        self.removeRoot(biggerRoot) # in O(1)

    def removeRoot(self,r): # in O(|roots|), actually is O(1)
        self.roots.remove(r)

    def cut(self,handle): # in O(deg(handle.parent)), for deleteMin in O(1), for decreaseKey in O(deg(handle.parent))
        if handle.parent is not None:
            if handle.parent.leftChild is not handle and handle.parent.leftChild is not None:
                currentElement = handle.parent.leftChild
                while currentElement.rightSibling is not handle:
                    currentElement = currentElement.rightSibling
                currentElement.rightSibling = None
            self.roots.append(handle)
            handle.parent = None
            handle.rightSibling = None

    def deleteMin(self): # in O(deg(root))=O(n)
        minValue = self.min()
        if self.minPtr is None or self.minPtr.leftChild is None: return minValue
        currentElement = self.minPtr.leftChild
        self.removeRoot(self.minPtr) # in O(1)
        while True:
            nextElement = currentElement.rightSibling
            self.cut(currentElement)
            self.minPtr.leftChild = nextElement
            if nextElement is None: break
            else: currentElement = nextElement
        for i in range(0,len(self.roots),2):
            if i+1 <= len(self.roots)-1: self.combine(self.roots[i],self.roots[i+1])
        while len(self.roots) > 1:
            self.combine(self.roots[len(self.roots)-1],self.roots[len(self.roots)-2])
        self.minPtr = self.roots[0]
        return minValue

    def decreaseKey(self,handle,value): #in O(deg(handle.parent))
        assert value <= handle.data
        handle.data = value
        if handle.parent is not None:
            self.cut(handle) # if Element is implemented with a previousSibling pointer O(1) is possible, else O(deg(handle.parent))
            self.combine(self.roots[0],self.roots[1])

    def merge(self,phB): # in O(1)
        assert len(phB.roots) == 1 and len(self.roots) == 1
        self.roots.append(phB.roots[0])
        self.combine(self.roots[0], self.roots[1])

    def remove(self,handle): # see decreaseKey
        self.decreaseKey(handle,float("-inf"))
        self.deleteMin()

ph = PairingHeap([3,2,4,2,3,4,6,8,3,4,87,5])
print(ph.deleteMin())
h = ph.minPtr.leftChild.leftChild
print(h.data)
print(h.parent)
ph.decreaseKey(h,1)
print(h.data)
print(h.parent)

