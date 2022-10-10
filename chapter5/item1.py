# มีรถไฟอยู่ขบวนหนึ่ง โดยรถไฟนั้นจะมีหมายเลขกำกับตู้แต่ละตู้อยู่และรถไฟก็มีหัวรถจักรอยู่
# แต่หัวรถจักรดันไปต่อกับตู้รถไฟอยู่ พี่ต้องการให้น้อง ๆ ทำการแบ่งขบวนรถไฟออก
# โดยให้หัวรถจักรอยู่ข้างหน้าสุด และส่วนตู้ที่เหลือให้ทำการต่อกับตู้สุดท้ายโดยไม่มีการเปลี่ยนลำดับของตู้
# ซึ่งพี่จะให้หมายเลข 0 แทนเป็นหัวรถจักร ส่วน หมายเลขอื่นจะเป็นตู้รถไฟ
# เช่น 2 <- 3 <- 1 <- 0 <- 4 <- 5 <- 6
# เป็น 0 <- 4 <- 5 <- 6 <- 2 <- 3 <- 1 ( ให้ใช้ singly linked list)

#  *** Locomotive ***
# Enter Input : 2 3 1 0 4 5 6
# Before : 2 <- 3 <- 1 <- 0 <- 4 <- 5 <- 6
# After : 0 <- 4 <- 5 <- 6 <- 2 <- 3 <- 1

#  *** Locomotive ***
# Enter Input : 1 2 3 0
# Before : 1 <- 2 <- 3 <- 0
# After : 0 <- 1 <- 2 <- 3


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

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
        for _ in range(index):
            t = t.next
        return t.value

    def __len__(self):
        return self.size

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

    def removeHead(self):
        if self.head != None:
            if self.head.next == None:
                p = self.head
                self.head = None
            else:
                p = self.head
                self.head = self.head.next
            self.size -= 1
        return p.value

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
