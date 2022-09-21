def hbd(year):
    base = float(year)//2
    age = 20 + int(year)%2 
    print("saimai is just " + str(int(age)) + ", in base " + str(int(base)) + "!")

year = input("Enter year : ")
hbd(year)

