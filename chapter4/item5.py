class Queue:
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def enQueue(self, i):
        self.items.append(i)

    def deQueue(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)
    
    def __str__(self):
        s = ''
        if self.isEmpty():
            s += 'Empty'
        else:
            for ele in self.items:
                s += str(ele) + ''
        return s

class Stack:
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def push(self, i):
        self.items.append(i)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def __str__(self):
        s = ''
        if self.isEmpty():
            s += 'Empty'
        else:
            for ele in self.items:
                s += str(ele) + ''
        return s

def isRepeat(s:Stack,i):
    if s.isEmpty() or s.peek() != i:
        return False
    elif s.size() > 1:
        bin = s.pop()
        if s.peek() == i:
            s.pop()
            return True
        else:
            s.push(bin)
            return False

nor, mir = map(list, input('Enter Input (Normal, Mirror) : ').split())
sn = Stack()
sm = Stack()
qb = Queue()
cnt_nor = 0
cnt_mir = 0
failed = 0

mir.reverse()
for i in mir:
    if not isRepeat(sm,i):
        sm.push(i)
    else:
        qb.enQueue(i)
        cnt_mir += 1

for i in nor:
    if not isRepeat(sn,i):
        sn.push(i)
    else:
        if not qb.isEmpty():
            if qb.peek() == i:
                sn.push(qb.deQueue())
                failed += 1
            else:
                sn.push(i)
                sn.push(i)
                sn.push(qb.deQueue())
                sn.push(i)
        else:
            cnt_nor += 1

print('NORMAL :')
print(sn.size())
if sn.isEmpty():
    print('Empty',end='')
else:
    for j in range(sn.size()):
        print(sn.pop(), end='')
print()
print(f'{cnt_nor} Explosive(s) ! ! ! (NORMAL)')
if failed > 0:
    print(f'Failed Interrupted {failed} Bomb(s)')
    
print('------------MIRROR------------\n: RORRIM')
print(sm.size())
if sm.isEmpty():
    print('ytpmE',end='')
else:
    for j in range(sm.size()):
        print(sm.pop(), end='')
print()
print(f'(RORRIM) ! ! ! (s)evisolpxE {cnt_mir}')