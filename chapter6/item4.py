def draw(n, a=[], b=[], c=[]):
    if n > 0:
        if n <= len(a):
            print(a[n - 1], end="  ")
        else:
            print("|", end="  ")
        if n <= len(b):
            print(b[n - 1], end="  ")
        else:
            print("|", end="  ")
        if n <= len(c):
            print(c[n - 1])
        else:
            print("|")
        return draw(n - 1, a, b, c)
    else:
        return


def move(n, A, C, B, maxn):
    if n == 1:
        if A == "A" and C == "C":
            c.append(a.pop())
        elif A == "B" and C == "C":
            c.append(b.pop())
        elif A == "A" and C == "B":
            b.append(a.pop())
        elif A == "C" and C == "B":
            b.append(c.pop())
        elif A == "B" and C == "A":
            a.append(b.pop())
        elif A == "C" and C == "A":
            a.append(c.pop())
        print(f"move {n} from  {A} to {C}")
        print("|  |  |")
        draw(maxn, a, b, c)
    else:
        move(n - 1, A, B, C, maxn)
        if A == "A" and C == "C":
            c.append(a.pop())
        elif A == "B" and C == "C":
            c.append(b.pop())
        elif A == "A" and C == "B":
            b.append(a.pop())
        elif A == "C" and C == "B":
            b.append(c.pop())
        elif A == "B" and C == "A":
            a.append(b.pop())
        elif A == "C" and C == "A":
            a.append(c.pop())
        print(f"move {n} from  {A} to {C}")
        print("|  |  |")
        draw(maxn, a, b, c)
        move(n - 1, B, C, A, maxn)


n = int(input("Enter Input : "))
a = list(range(n, 0, -1))
b = list()
c = list()
print("|  |  |")
draw(n, a, b, c)
move(n, "A", "C", "B", n)
