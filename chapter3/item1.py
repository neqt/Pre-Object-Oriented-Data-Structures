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
    if i[0] == 'A':
        i = i.replace('A ','')
        S.push(i)
        print('Add = ' + str(i) + ' and Size = ' + str(S.size()))
    elif i[0] == 'P':
        if S.isEmpty():
            print('-1')
        else:
            print('Pop = ' + str(S.pop()) + ' and Index = ' + str(S.size()))
print(S)
