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
        return 'Value in Stack = ' + str(S1.items)

def ManageStack(inputList):
    for i in inputList:
        i = i.split()
        if i[0] == 'A':
            S1.push(int(i[1]))
            print('Add = ' + str(i[1]))
        elif i[0] == 'P':
            if S1.isEmpty():
                print('-1')
            else:
                print('Pop = ' + str(S1.peek()))
                S1.pop()
        elif i[0] == 'D':
            if S1.isEmpty():
                print('-1')
            else:
                for j in range(S1.size()):
                    if int(i[1]) != int(S1.peek()):
                        S2.push(S1.pop())
                    else:
                        print('Delete = ' + str(S1.peek()))
                        S1.pop()
                for k in range(S2.size()):
                    S1.push(S2.pop())
        elif i[0] == 'LD':
            if S1.isEmpty():
                print('-1')
            else:
                for j in range(S1.size()):
                    if int(i[1]) <= int(S1.peek()):
                        S2.push(S1.pop())
                    else:
                        print('Delete = ' + str(S1.peek()) + ' Because ' + str(S1.peek()) + ' is less than ' + str(i[1]))
                        S1.pop()
                for k in range(S2.size()):
                    S1.push(S2.pop())
        elif i[0] == 'MD':
            if S1.isEmpty():
                print('-1')
            else:
                for j in range(S1.size()):
                    if int(i[1]) >= int(S1.peek()):
                        S2.push(S1.pop())
                    else:
                        print('Delete = ' + str(S1.peek()) + ' Because ' + str(S1.peek()) + ' is more than ' + str(i[1]))
                        S1.pop()
                for k in range(S2.size()):
                    S1.push(S2.pop())
    return print(S1)

S1 = Stack()
S2 = Stack()
inp = input('Enter Input : ').split(',')
ManageStack(inp)