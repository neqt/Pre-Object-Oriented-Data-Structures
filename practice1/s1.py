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
        return str(self.items)

# s = Stack()
# inp = input('Enter Eqaution : ')
# state = 0

# for i in inp:
#     if i == '(' or i == '{' or i == '[':
#         s.push(i)
#     elif i == ')' or i == '}' or i == ']':
#         # print('i' + s.peek() + ' pop'+ i)
#         if s.peek() == '(' and i == ')' or s.peek() == '{' and i == '}' or s.peek() == '[' and i == ']':
#             s.pop()

# # print(s)
# if not s.isEmpty():
#     print('Error')
# else:
#     print('Complete')

# op = "([{"
# cl = ")]}"
# s = Stack()    
# inp = input("Enter expresion : ")
# for i in inp:
#     if i in op:
#         s.push(i)
#     elif i in cl:
#         if s.isEmpty():
#             print(" close paren excess")
#             break
#         elif op.index(s.peek()) != cl.index(i):
#             print(" Unmatch open-close")
#             break
#         else:
#             s.pop()

# if not s.isEmpty():
#     print(" open paren excess   {0} : ".format(s.size()), end= "")
#     t = ""
#     while not s.isEmpty():
#         t += s.pop()
#     print(t[::-1])

inp = input('Enter Input : ')
s = Stack()
ope = '([{'
clo = ')]}'

for i in inp:
    if i in ope:
        s.push
