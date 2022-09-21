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

def dec2bin(decnum):
    s = Stack()
    cnt = 0
    while decnum > 0:
        s.push(decnum%2)
        decnum //= 2
    while not s.isEmpty():
        print(s.pop(), end='')
    return ''

print(" ***Decimal to Binary use Stack***")
token = input("Enter decimal number : ")
print("Binary number : ", end='')
print(dec2bin(int(token)))