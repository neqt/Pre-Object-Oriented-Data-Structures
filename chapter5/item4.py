class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        s = ""
        t = self.head
        if self.head == None:
            return "Empty"
        while t != None:
            s += str(t.data)
            t = t.next
            if t != None:
                s += "->"
        return s

    def __getitem__(self, index):
        t = self.head
        for _ in range(index):
            t = t.next
        return t

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

    def search(self, item):
        t = self.head
        while t != None:
            if t.data == item:
                return "Found"
            t = t.next
        return "Not Found"

    def index(self, item):
        cnt = 0
        t = self.head
        while t != None:
            if t.data == item:
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
inp = input("Enter input : ").split(",")
isLoop = False

for i in inp:
    i = i.split()
    if i[0] == "A":
        l.append(i[1])
        print(l)
    elif i[0] == "S":
        i[1] = i[1].split(":")
        if l.isEmpty():
            print("Error! {list is empty}")
        else:
            if int(i[1][0]) >= l.size():
                print("Error! {index not in length}:", int(i[1][0]))
            elif int(i[1][1]) >= l.size():
                l.append(int(i[1][1]))
                print("index not in length, append :", int(i[1][1]))
            else:
                h1 = l[int(i[1][0])]
                h2 = l[int(i[1][1])]
                h1.next = h2
                if i[1][0] >= i[1][1]:
                    isLoop = True
                print(
                    f"Set node.next complete!, index:value = {i[1][0]}:{h1.data} -> {i[1][1]}:{h2.data}"
                )
                
if isLoop:
    print("Found Loop")
else:
    print("No Loop")
    print(l)
