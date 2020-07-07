I = input()
while I != '*':
    words = I.split()
    firstLetter = words[0][0].upper()
    tautogram = True
    for i in range(1, len(words)):
        if words[i][0].upper() != firstLetter:
            tautogram = False
            break

    if tautogram:
        print('Y')
    else:
        print('N')

    I = input()
