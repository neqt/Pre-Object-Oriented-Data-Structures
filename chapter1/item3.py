print(" *** Summation of each digit ***")
n = input("Enter a positive number : ")

sum = 0
for d in str(n):
    sum += int(d)

print("Summation of each digit =  " + str(sum))

