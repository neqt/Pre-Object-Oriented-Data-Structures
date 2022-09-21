class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        s = ""
        t = self.head
        while t != None:
            s += str(t.value)
            t = t.next
            if t != None:
                s += " <- "
        return s

    def __getitem__(self, index):
        t = self.head
        for i in range(index):
            t = t.next
        return t.value

    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False

    def append(self, item):
        p = Node(item)
        if self.head == None:
            self.head = p
            self.tail = p
        else:
            t = self.head
            while t.next != None:
                t = t.next
            t.next = p
            self.tail.next = p
            self.tail = p

    def removeHead(self):
        self.head = self.head.next

    def search(self, item):
        t = self.head
        while t != None:
            if t.value == item:
                return "Found"
            t = t.next
        return "Not Found"

    def index(self, item):
        cnt = 0
        t = self.head
        while t != None:
            if t.value == item:
                return cnt
            t = t.next
            cnt += 1
        return -1

    def size(self):
        size = 0
        t = self.head
        while t != None:
            size += 1
            t = t.next
        return size


l = LinkedList()
inp = [int(n) for n in input(" *** Locomotive ***\nEnter Input : ").split()]

for i in inp:
    l.append(i)

print("Before :", l)

for i in range(l.index(0)):
    l.append(l[0])
    l.removeHead()

print("After :", l)


# def pop(self, pos):
#     n = self.size()
#     i = 0
#     t = self.head
#     while i < pos and pos < n:
#         t = t.next
#         i += 1
#     if n == 1:
#         self.head = None
#         self.previous = None
#     elif i == 0:
#         self.head = t.next
#         self.head.previous = None
#     elif i == n - 1:
#         self.tail = t.previous
#         self.tail.next = None
#     else:
#         t.next.previous = t.previous
#         t.previous.next = t.next

# def addHead(self, item):
#     p = Node(item)
#     if self.head == None:
#         self.head = p
#     else:
#         p.next = self.head
#         self.head.previous = p
#         self.head = p

# def addTail(self, item):
#     p = Node(item, None)
#     self.tail.next == p
#     self.tail = p

# def removeTail(self):
#     t = self.head
#     while t.next.next != None:
#         t = t.next
#     t.next = t.next.next

# def moveHead(self):
#     t = self.head
#     while t.next.value != 0:
#         t = t.next
#     self.tail.next = self.head
#     self.tail = self.head
#     self.head = t.next
#     self.tail = t
#     t.next = None
