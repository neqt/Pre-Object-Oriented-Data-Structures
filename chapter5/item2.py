class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        s = "linked list : "
        t = self.head
        if self.isEmpty():
            return s
        else:
            while t != None:
                s += str(t.data)
                t = t.next
                if t != None:
                    s += "->"
        return s

    def str_reverse(self):
        s = "reverse : "
        t = self.tail
        if self.isEmpty():
            return s
        else:
            while t != None:
                s += str(t.data)
                t = t.previous
                if t != None:
                    s += "->"
        return s

    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False

    def append(self, data):
        p = Node(data)
        if self.isEmpty():
            self.head = p
            self.tail = p
        else:
            p.previous = self.tail
            self.tail.next = p
            self.tail = p

    def insert(self, index, data):
        p = Node(data)
        if index < 0 or index > self.size():
            return "Data cannot be added"
        else:
            if index == self.size():
                self.append(data)
            elif index == 0:
                if self.isEmpty():
                    self.head = p
                else:
                    p.next = self.head
                    self.head.previous = p
                    self.head = p
            else:
                t = self.head
                for _ in range(index - 1):
                    if t.next == None:
                        break
                    t = t.next
                p.next = t.next
                t.next.previous = p
                t.next = p
                p.previous = t
            return f"index = {index} and data = {data}"

    def remove(self, data):
        index = 0
        t = self.head
        while t != None:
            if int(t.data) == int(data):
                if t.previous == None and t.next == None:
                    self.head = None
                elif t.previous == None and t.next != None:
                    self.head = t.next
                    self.head.previous = None
                elif t.previous != None and t.next == None:
                    t.previous.next = None
                else:
                    t.previous.next = t.next
                    t.next.previous = t.previous
                return f"removed : {data} from index : {index}"
            t = t.next
            index += 1
        return "Not Found!"

    def size(self):
        size = 0
        t = self.head
        while t != None:
            size += 1
            t = t.next
        return size


l = DoublyLinkedList()
inp = input("Enter Input : ").split(",")
for i in inp:
    i = i.split()
    if i[0] == "A":
        l.append(i[1])
    elif i[0] == "Ab":
        l.insert(0, int(i[1]))
    elif i[0] == "I":
        i[1] = i[1].split(":")
        print(l.insert(int(i[1][0]), int(i[1][1])))
    elif i[0] == "R":
        print(l.remove(i[1]))
    print(l)
    print(l.str_reverse())
