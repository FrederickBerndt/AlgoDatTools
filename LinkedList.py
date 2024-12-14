class ListElement:
    def __init__(self,d,n=None):
        self.data = d
        self.next = n

class SinglyLinkedList:
    def __init__(self,a=[]):
        self.dummy = ListElement(float("inf"))
        self.dummy.next = self.dummy
        for e in range(len(a)):
            self.insertAfter(e,self.dummy)

    def insertAfter(self,data,handle):
        newElement = ListElement(data)
        newElement.next = handle.next
        handle.next = newElement

    def find(self,x):
        self.dummy.data = x
        currentElement = self.dummy.next
        while currentElement.data != x:
            currentElement = currentElement.next
        self.dummy.data = float("inf")
        if currentElement is self.dummy: return None

    def remove(self,x):
        self.dummy.data = x
        currentElement = self.dummy.next
        if currentElement is self.dummy: return None
        if currentElement.data == x and currentElement.next is self.dummy:
            self.dummy.next = self.dummy
        previousElement = self.dummy
        while currentElement.data != x:
            currentElement = currentElement.next