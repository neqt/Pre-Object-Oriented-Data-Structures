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
        q = ''
        if self.isEmpty():
            q += 'Empty'
        else:
            for ele in self.items:
                q += str(ele) + ' '
        return q

q = Queue()
q1 = Queue()
q2 = Queue()
peop,time = input('Enter people and time : ').split()

for j in peop:
    q.enQueue(j)

for i in range(int(time)):
    if not q.isEmpty():
        if q1.isEmpty():
            q1.enQueue(q.deQueue())
        elif q1.size() < 5:
            if i % 3 == 0:
                q1.deQueue()
                q1.enQueue(q.deQueue())
            else:
                q1.enQueue(q.deQueue())
        else:
            if i % 3 == 0:
                q1.deQueue()
                q1.enQueue(q.deQueue())
            else:
                if q2.isEmpty():
                    q2.enQueue(q.deQueue())
                elif q2.size() < 5:
                    if i % 2 == 0:
                        q2.enQueue(q.deQueue())
                    else:
                        q2.deQueue()
                        q2.enQueue(q.deQueue())
        if not q2.isEmpty() and not q.isEmpty():
            if i % 3 == 0:
                if i % 2 == 1:
                    q2.deQueue()
    else:
        if not q1.isEmpty():
            if i % 3 == 0:
                q1.deQueue()
        if not q2.isEmpty():
            if i % 3 == 0:
                if i % 2 == 1:
                    q2.deQueue()
            else:
                q2.deQueue()

    print(str(i+1),end=' ')
    print(q.items,end=' ')
    print(q1.items,end=' ')
    print(q2.items,end=' ')
    print()