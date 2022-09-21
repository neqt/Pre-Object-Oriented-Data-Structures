class node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


def createList(l=[]):
    head = p = node(l[0])
    for i in range(1, len(l)):
        p.next = node(l[i])
        p = p.next
    return head


def printList(H):
    s = ""
    while H != None:
        s += str(H.data) + " "
        H = H.next
    print(s)


def mergeOrderesList(p, q):
    head = cur = node()
    while p != None or q != None:
        if p == None:
            cur.next = q
            q = q.next
        elif q == None:
            cur.next = p
            p = p.next
        elif int(p.data) <= int(q.data):
            cur.next = p
            p = p.next
        else:
            cur.next = q
            q = q.next
        cur = cur.next
    return head.next


L1, L2 = input("Enter 2 Lists : ").split()
LL1 = createList(L1.split(","))
LL2 = createList(L2.split(","))
print("LL1 : ", end="")
printList(LL1)
print("LL2 : ", end="")
printList(LL2)
m = mergeOrderesList(LL1, LL2)
print("Merge Result : ", end="")
printList(m)
