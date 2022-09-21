print(" *** Wind classification ***")
s = float(input("Enter wind speed (km/h) : "))

# if(s >= 209):
#     print("Wind classification is Super Typhoon.")
# elif(s >= 102.00 and s <= 208.99):
#     print("Wind classification is Typhoon.")
# elif(s >= 56.00 and s <= 101.99):
#     print("Wind classification is Tropical Storm.")
# elif(s >= 52.00 and s <= 55.99):
#     print("Wind classification is Depression.")
# elif(s >= 0 and s <= 51.99):
#     print("Wind classification is Breeze.")

if s >= 209:
    print("Wind classification is Super Typhoon.")
elif s >= 102.00 and s <= 208.99:
    print("Wind classification is Typhoon.")
elif s >= 56.00 and s <= 101.99:
    print("Wind classification is Tropical Storm.")
elif s >= 52.00 and s <= 55.99:
    print("Wind classification is Depression.")
elif s >= 0 and s <= 51.99:
    print("Wind classification is Breeze.")