def bon(w):
    cntRepeat = 0
    cntAlph = 0
    code = 0
    char = ''
    alph = []

    for a in range(97,123):
        alph.append(chr(a))

    for i in w[1:]:
        if i == w[cntRepeat]:
            char = i
            break
        cntRepeat += 1

    for j in alph:
        if char == j:
            code = (cntAlph+1) * 4
        cntAlph += 1

    return code

secretCode = input("Enter secret code : ")
print(bon(secretCode))