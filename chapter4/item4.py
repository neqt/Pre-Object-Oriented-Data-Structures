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
        cnt = 0
        for ele in self.items:
            q += str(ele)
            cnt += 1
            if cnt < len(self.items):
                q += ', '
        return q

qm = Queue()
qy = Queue()

inp = input('Enter Input : ').split(',')
for i in inp:
    i = i.split()
    if i[0]:
        qm.enQueue(i[0])
    if i[1]:
        qy.enQueue(i[1])

print('My   Queue = ', end='')
print(qm)
print('Your Queue = ', end='')
print(qy)

print('My   Activity:Location = ', end='')
cnt_my = 0
for j in qm.items:
    act = ''
    loc = ''
    j = j.split(':')
    if j[0] == '0':
        act += 'Eat'
    elif j[0] == '1':
        act += 'Game'
    elif j[0] == '2':
        act += 'Learn'
    elif j[0] == '3':
        act += 'Movie'
    if j[1] == '0':
        loc += 'Res.'
    elif j[1] == '1':
        loc += 'ClassR.'
    elif j[1] == '2':
        loc += 'SuperM.'
    elif j[1] == '3':
        loc += 'Home'
    print(act + ':' + loc, end='')
    cnt_my += 1
    if cnt_my < len(qm.items):
        print(', ', end='')
print()

cnt_yo = 0
print('Your Activity:Location = ', end='')
for j in qy.items:
    act = ''
    loc = ''
    j = j.split(':')
    if j[0] == '0':
        act += 'Eat'
    elif j[0] == '1':
        act += 'Game'
    elif j[0] == '2':
        act += 'Learn'
    elif j[0] == '3':
        act += 'Movie'
    if j[1] == '0':
        loc += 'Res.'
    elif j[1] == '1':
        loc += 'ClassR.'
    elif j[1] == '2':
        loc += 'SuperM.'
    elif j[1] == '3':
        loc += 'Home'
    print(act + ':' + loc, end='')
    cnt_yo += 1
    if cnt_yo < len(qy.items):
        print(', ', end='')
print()

score = 0
for k in range(len(inp)):
    if qm.peek()[0] == qy.peek()[0]:
        if qm.peek()[2] == qy.peek()[2]:
            score += 4
        else:
            score += 1
    else:
        if qm.peek()[2] == qy.peek()[2]:
            score += 2
        else:
            score -= 5
    qm.deQueue()
    qy.deQueue()

if score >= 7:
    print(f"Yes! You're my love! : Score is {score}.")
elif score > 0:
    print(f"Umm.. It's complicated relationship! : Score is {score}.")
else:
    print(f"No! We're just friends. : Score is {score}.")
