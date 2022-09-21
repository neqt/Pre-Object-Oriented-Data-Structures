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
inp = input('Enter Input : ').split(',')
for i in inp:
    i = i.split()
    if i[0] == 'E':
        q.enQueue(i[1])
        print(q.size())
    if i[0] == 'D':
        if q.isEmpty():
            print('-1')
        else:
            print(q.deQueue() + ' 0')
print(q)
