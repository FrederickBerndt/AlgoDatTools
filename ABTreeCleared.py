def key(element):
    return element

class Item:
    def __init__(self, element, next=None, prev=None):
        self.element = element
        self.next = next if next is not None else self
        self.prev = prev if prev is not None else self

    def __repr__(self):
        return str(self.element)

    def invarianten(self):
        assert self.next.prev == self, f"next.prev {self.next.prev} ist nicht {self}"
        assert self.prev.next == self, f"prev.next {self.prev.next} ist nicht {self}"
        return True
    

class DLList:
    def __init__(self, elements = None):
        self.length = 0
        self.head = Item(None)
        if elements is not None:
            for element in elements:
                self.insertBefore(self.head, element)

    def __repr__(self):
        return "[" + ", ".join(str(item) for item in self) + "]"

    def insertAfter(self, item, element):
        new_item = Item(element)
        fort = item.next
        item.next = new_item
        new_item.next = fort
        fort.prev = new_item
        new_item.prev = item
        self.length += 1
        return new_item

    def insertBefore(self, item, element):
        return self.insertAfter(item.prev, element)

    def remove(self, item):
        item.prev.next = item.next
        item.next.prev = item.prev
        self.length -= 1

    def __len__(self):
        return self.length

    def __iter__(self):
        item = self.head.next
        while item != self.head:
            yield item
            item = item.next

class ABItem:
    def __init__(self, a, b, splitters, children):
        self.a = a
        self.b = b
        self.d = len(children)
        self.splitter = splitters
        self.children = children

    def __repr__(self):
        res = str(self.splitter) + '\n' + str(self.children) + '\n'
        return res

    def locateLocally(self, element) -> int:
        return min([i for i in range(self.d-1) if key(element) <= self.splitter[i]], default=self.d-1)

    def locateRec(self, value: int, height: int):
        index = self.locateLocally(value)
        if height == 1:
            if self.children[index].element >= value:
                return self.children[index]
            else:
                return self.children[index].next
        else:
            return self.children[index].locateRec(value, height - 1)

    def insertRec(self, element, height: int, liste: DLList):
        index = self.locateLocally(element)
        if height == 1:
            if key(self.children[index].element) == key(element):
                self.children[index].element = element
                return (None, None)
            else:
                if key(self.children[index].element) > key(element):
                    (value, pointer) = (key(element), liste.insertBefore(self.children[index], element))
                else:
                    (value, pointer) = (key(self.children[index].element), liste.insertAfter(self.children[index], element))
                    tmp = self.children[index]
                    self.children[index] = pointer
                    pointer = tmp
        else:
            (value, pointer) = self.children[index].insertRec(element, height - 1, liste)
            if pointer is None:
                return (None, None)

        s_dash = self.splitter[:index] + [value] + self.splitter[index:]
        c_dash = self.children[:index] + [pointer] + self.children[index:]

        if self.d < self.b:
            (self.splitter, self.children, self.d) = (s_dash, c_dash, self.d + 1)
            return (None, None)
        else:
            self.d = (self.b + 1) // 2
            self.splitter = s_dash[self.b + 1 - self.d:]
            self.children = c_dash[self.b + 1 - self.d:]

            return (
                s_dash[self.b - self.d],
                ABItem( self.a, self.b,
                    s_dash[: self.b - self.d], c_dash[: self.b - self.d + 1]
                ),
            )

    def removeRec(self, element, height: int, liste: DLList):
        index = self.locateLocally(element)
        if height == 1:
            if key(self.children[index].element) == key(element):
                liste.remove(self.children[index])
                self.removeLocally(index)
        else:
            self.children[index].removeRec(element, height-1, liste)
            if self.children[index].d < self.children[-1].a:
                if index+1 == self.d: index -= 1
                s_dash = self.children[index].splitter + [self.splitter[index]] + self.children[index+1].splitter
                c_dash = self.children[index].children + self.children[index+1].children
                d_dash = len(c_dash)
                if d_dash <= self.b:
                    (self.children[index+1].splitter, self.children[index+1].children, self.children[index+1].d) = (s_dash, c_dash, d_dash)
                    self.removeLocally(index)
                else:
                    m = int(-(-d_dash//2))
                    (self.children[index].splitter, self.children[index].children, self.children[index].d) = (s_dash[:m-1], c_dash[:m], m)
                    (self.children[index+1].splitter, self.children[index+1].children, self.children[index+1].d) = (s_dash[m+1-1:d_dash-1], c_dash[m+1-1:d_dash], d_dash-m)
                    self.splitter[index] = s_dash[m-1]

    def removeLocally(self, index):
        del self.children[index]
        if index >= len(self.splitter)-1:
            del self.splitter[-1]
        else: del self.splitter[index]
        self.d -= 1

    def __iter__(self):
        for child in self.children:
            if hasattr(child, "children"):
                yield from child
            else:
                yield child

class ABTree:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b
        self.liste = DLList([float("inf")])
        self.root = ABItem(2, self.b, [], [self.liste.head.next])
        self.height = 1

    def locate(self, value):
        return self.root.locateRec(value, self.height)

    def insert(self, element):
        (value, pointer) = self.root.insertRec(element, self.height, self.liste)
        if pointer is not None:
            self.root.a = self.a                        
            self.root = ABItem(2, self.b, [value], [pointer, self.root])
            self.height += 1

    def remove(self, element):
        self.root.removeRec(element, self.height, self.liste)
        if self.root.d == 1 and self.height > 1:
            r_ = self.root
            self.root = r_.children[0]
            self.height -= 1

    def __repr__(self):
        levl = [self.root]
        res = ""
        while levl:
            res += str(levl) + "\n"
            levl = [child for item in levl for child in item.children if hasattr(child, "children")]
        return res
    
import random
for _ in range(10):
    a = random.randint(2, 2)
    b = random.randint(a*2, a*2)
    tree = ABTree(a, b)
    for _ in range(100):
        rkey = random.randint(0, 10)
        if random.random() < 0.8:
            tree.insert(rkey)
        else:
            tree.remove(rkey)