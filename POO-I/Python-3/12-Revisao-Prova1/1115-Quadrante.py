x, y = [int(w) for w in input().split()]

while x != 0 and y != 0:
    if x > 0:
        if y > 0:
            print('primeiro')
        else:
            print('quarto')
    elif y > 0:
        print('segundo')
    else:
        print('terceiro')
    x, y = [int(w) for w in input().split()]
