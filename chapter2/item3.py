def mod_position(arr, s):
    cnt = 0
    total = []
    for i in s:
        if (cnt+1)%int(arr) == 0:
            total.append(i)
        cnt += 1
    return total

print("*** Mod Position ***")
s,n = input("Enter Input : ").split(",")
print(mod_position(n,s))