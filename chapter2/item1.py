def Rshift(num, shift):
    r = num // (2 ** shift)
    return r

n, s = input("Enter number and shiftcount : ").split()
print(Rshift(int(n),int(s)))
