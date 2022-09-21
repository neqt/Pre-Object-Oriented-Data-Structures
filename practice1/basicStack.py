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
        return self.items == None

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

inp = input('Enter Input : ').split(',')
s = Stack()

for i in inp:
    i = i.split()
    if i[0] == 'A':
        s.push(i[1])
        print(f'Add = {i[1]} and Size = {s.size()}')
    elif i[0] == 'P':
        print(f'Pop = {s.pop()} and Index = {s.size()}')
print(s)