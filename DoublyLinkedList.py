class Element:
    def __init__(self,x,p=None,n=None):
        self.data = x
        self.previous = p
        self.next = n

class DoublyLinkedList:
    def __init__(self,a=[]):
        self.dummy = Element(float("inf"))
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
