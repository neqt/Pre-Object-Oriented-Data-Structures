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
                s += " "
        return s

    def __getitem__(self, index):
        t = self.head
        for _ in range(index):
            t = t.next
        return t.data

    def print(self):
        s = ""
        t = self.head
        if self.isEmpty():
            return "Empty"
        while t != None:
            s += str(t.data)
            t = t.next
            if t != None:
                s += " -> "
        return s

    def isEmpty(self):
        return self.head == None

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

    def addHead(self, item):
        p = Node(item)
        if self.isEmpty():
            self.head = p
            self.tail = p
        else:
            t = self.head
            p.next = self.head
            t.previous = p
            self.head = p
            while t.next != None:
                t = t.next
            self.tail = t

    def insert(self, pos, item):
        p = Node(item)
        if int(pos) == 0:
            p.next = self.head
            self.head = p
        else:
            q = self.head
            for _ in range(int(pos) - 1):
                q = q.next
            p.next = q.next
            q.next = p

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

    def deQueue(self):
        t = self.head
        q = self.head.data
        if t.next == None:
            self.head = None
        else:
            self.head = t.next
        return q

    def pop(self):
        t = self.head
        if t.next == None:
            self.head = None
            self.tail = None
        else:
            self.head = t.next


def radix_sort(inp):
    l = LinkedList()
    for i in inp:
        l.append(i)

    ll = LinkedList()
    for _ in range(10):
        ll.append(LinkedList())

    rnd = 1
    while 1:
        while not l.isEmpty():
            num = l.deQueue()
            ind = get_digit(abs(int(num)), rnd)
            if ll[ind].isEmpty():
                ll[ind].append(num)
            else:
                for i in range(ll[ind].size()):
                    if int(ll[ind][i]) <= int(num):
                        ll[ind].insert(i, num)
                        break
                    else:
                        if i == ll[ind].size() - 1:
                            ll[ind].append(num)

        print("Round :", rnd)
        for cnt in range(10):
            print(cnt, ": ", end="")
            if ll[cnt].isEmpty():
                print()
            else:
                print(ll[cnt])
        print("------------------------------------------------------------")

        isEnd = True
        for i in range(1, 10):
            if not ll[i].isEmpty():
                isEnd = False
        for i in range(10):
            while not ll[i].isEmpty():
                l.append(ll[i].deQueue())
        if isEnd:
            return l, rnd - 1
        rnd += 1
    return l, rnd - 2


def get_digit(n, d):
    for _ in range(d - 1):
        n //= 10
    return n % 10


l = LinkedList()
inp = input("Enter Input : ").split()
for i in inp:
    l.append(i)

print("------------------------------------------------------------")
a, time = radix_sort(inp)
print(time, "Time(s)")
print(f"Before Radix Sort : {l.print()}")
print(f"After  Radix Sort : {a.print()}")
