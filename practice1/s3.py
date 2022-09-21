class MaxStack:
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
        self.maxValue =None

    def push(self, i:int):
        self.items.append(i)
        if self.maxValue == None or i > self.maxValue:
            self.maxValue = i

    def pop(self):
        if not self.isEmpty():
            p = self.items.pop()
            if p == self.maxValue:
                newMax = self.items[0]
                for i in self.items:
                    if i > newMax:
                        newMax = i
                self.maxValue = newMax
            return p

    def peek(self):
        return self.items[-1]
    
    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def max(self):
        if not self.isEmpty():
            return self.maxValue

    def __str__(self):
        return str(self.items)

# inp = input('Enter Number : ').split()
# s = MaxStack()

# for i in inp:
#     if s.isEmpty():
#         s.push(i)
#     else:
#         if s.peek() <= i:
#             numMax = i
#             s.push(i)
#         else:
#             s.push(i)

# print('Ypur number is : ', s)
# print('Max is : ', s.max())


# class Stack:
#     def __init__(self):
#         self.items = []
#         self.max_value = None

#     def __str__(self):
#         return ",".join(list(map(str, self.items)))

#     def push(self, e:int):
#         self.items.append(e)
#         if self.max_value is None or e > self.max_value:
#             self.max_value = e

#     def pop(self):
#         if not self.is_empty():
#             e = self.items.pop()
#             if self.is_empty():
#                 self.max_value = None
#             else:
#                 if e == self.max_value:
#                     new_max = self.items[0]
#                     for i in self.items:
#                         if i > new_max:
#                             new_max = i
#                     self.max_value = new_max
#         return e

#     def max(self):
#         if not self.is_empty():
#             return self.max_value

#     def is_empty(self):
#         return len(self.items) == 0

inp = input("Enter Input : ").split(",")
s = MaxStack()
for e in inp:
    if e == "PO":
        print("POP:", s, "->", s.pop())
    elif e == "MX":
        print("MAX:", s.max())
    else:
        a, b = e.split()
        if a == "PU":
            s.push(b)
            print("PUSH:", s)