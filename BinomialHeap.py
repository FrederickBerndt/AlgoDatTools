class Node:
    def __init__(self,d,p=None,l=None,s=None,r=0):
        self.data = d
        self.parent = p
        self.leftChild = l
        self.rightSibling = s
        self.rank = r

class BinomialHeap:
    def __init__(self,a):
        self.minPtr = None
        self.root = None
        for e in a: self.insert(e)

    def merge(self,leftRoot,rightRoot):
        assert leftRoot.rank == rightRoot.rank
        if leftRoot.data < rightRoot.data: 
            smallerRoot = leftRoot
            largerRoot = rightRoot
        else:
            smallerRoot = rightRoot
            largerRoot = leftRoot
        largerRoot.parent = smallerRoot
        ####min Pointer Update
        largerRoot.rightSibling = smallerRoot.leftChild
        smallerRoot.leftChild = largerRoot
        smallerRoot.rightSibling = rightRoot.rightSibling
        smallerRoot.rank += 1
        if smallerRoot.rightSibling is not None and smallerRoot.rightSibling.rank == smallerRoot.rank:
            return self.merge(smallerRoot, smallerRoot.rightSibling)
        else: return smallerRoot

    def min(self):
        if self.minPtr is not None: return self.minPtr.data
        else: return float("inf")    

    def insert(self,e):
        newNode = Node(e)
        newNode.rightSibling = self.root
        self.root = newNode
        if self.min() >= e: self.minPtr = newNode
        if self.root.rightSibling is not None and self.root.rightSibling.rank == 0: 
            self.root = self.merge(self.root,self.root.rightSibling)

bh = BinomialHeap([1,2,3,4,5,6,7])
print("hehe bh")
