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
        return str(self.items)

def encodemsg(q1, q2):
    value = 0
    re = 0
    for i in range(q1.size()):
        value = ord(q1.peek()) + int(q2.peek())
        if ord(q1.peek()) > 96:
            if value > 122:
                value -= 26
        else:
            if value > 90:
                value -= 26
        q1.enQueue(chr(value))
        q1.deQueue()
        q2.enQueue(q2.deQueue())

    if q1.size() % q2.size() != 0:
        re = q1.size() % q2.size()
        re = q2.size() - re
    for j in range(re):
        q2.enQueue(q2.deQueue())
    print(q1)

def decodemsg(q1, q2):
    value = 0
    re = 0
    for i in range(q1.size()):
        value = ord(q1.peek()) - int(q2.peek())
        if ord(q1.peek()) > 96:
            if value < 97:
               value += 26
        else:
            if value < 65:
               value += 26
        q1.enQueue(chr(value))
        q1.deQueue()
        q2.enQueue(q2.deQueue())

    if q1.size() % q2.size() != 0:
        re = q1.size() % q2.size()
        re = q2.size() - re
    for j in range(re):
        q2.enQueue(q2.deQueue())
    print(q1)

q1 = Queue()
q2 = Queue()
s,n = input('Enter String and Code : ').split(',')
for i in s:
    if i != ' ':
        q1.enQueue(i)
for i in n:
    q2.enQueue(i)

print('Encode message is :  ', end='')
encodemsg(q1, q2)
print('Decode message is :  ', end='')
decodemsg(q1, q2)