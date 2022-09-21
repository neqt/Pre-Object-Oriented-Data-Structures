print("*** Fun with Drawing ***")
n = int(input("Enter input : "))
if n >= 2:
    for i in range(n):
        for j in range(n-i-1):
            print('.', end='')
        print("*", end='')
        for j in range(i*2-1):
            print('+', end='')
        if i != 0:
            print('*', end='')
        for j in range((n-i)*2-3):
            print('.', end='')
        if i != n-1:
            print('*', end='')
        for j in range(i*2-1):
            print('+', end='')
        if i != 0:
            print('*', end='')
        for j in range(n-i-1):
            print('.', end='')
        print()
    for i in range(n*2-2):
        for j in range(i+1):
            print('.', end='')
        print('*', end='')
        for j in range(n*2-i-3):
            print('+', end='')
        for j in range(n*2-i-4):
            print('+', end='')
        if i != n*2-3:
            print('*', end='')
        for j in range(i+1):
            print('.', end='')
        print()

    # for i in range(n):
    #     for j in range(n):
    #         if i+j < n+n-6:
    #             print('.', end='')
    #         elif i+j == n+n-6:
    #             print('*', end='') 
    #         else:
    #             print('+', end='')
    #     for j in range(n-1):
    #         if i-j < 1:
    #             print('.', end='')
    #         elif i-j == 1:
    #             print('*', end='')
    #         else:
    #             print('+', end='')
    #     for j in range(n-1):
    #         if i+j < n+n-7:
    #             print('.', end='')
    #         elif i+j == n+n-7:
    #             print('*', end='') 
    #         else:
    #             print('+', end='')
    #     for j in range(n-1):
    #         if i-j < 1:
    #             print('.', end='')
    #         elif i-j == 1:
    #             print('*', end='')
    #         else:
    #             print('+', end='')
    #     print()
    # for i in range(n*2-2):
    #     for j in range(n*2-1):
    #         if i-j < -1:
    #             print('+', end='')
    #         elif i-j == -1:
    #             print('*', end='')
    #         else:
    #             print('.', end='')
    #     for j in range(n*2-2):
    #         if i+j < n+n-4:
    #             print('+', end='')
    #         elif i+j == n+n-4:
    #             print('*', end='') 
    #         else:
    #             print('.', end='')
    #     print()
