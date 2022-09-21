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
        s = 'Value in Stack = '
        if self.isEmpty():
            s += 'Empty'
        else:
            for ele in self.items:
                s += str(ele) + ' '
        return s

S = Stack()
inp = input('Enter Input : ').split(',')
for i in inp:
    i = i.split()
    if i[0] == 'A':
        if S.isEmpty():
            S.push(i[1])
        else:
            for j in range(S.size()):
                if int(i[1]) >= int(S.peek()):
                    S.pop()
            S.push(i[1])
    elif i[0] == 'B':
        if S.isEmpty():
            print('0')
        else:
            print(S.size())
