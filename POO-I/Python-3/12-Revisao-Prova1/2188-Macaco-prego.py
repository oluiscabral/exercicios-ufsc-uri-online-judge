N = int(input())

counter = 1
while N != 0:
    compare_X = 0
    compare_Y = 0
    compare_U = 0
    compare_V = 0
    has_compare = False
    valid = True
    for i in range(N):
        X, Y, U, V = [int(w) for w in input().split()]
        if not has_compare:
            has_compare = True
            compare_X = X
            compare_Y = Y
            compare_U = U
            compare_V = V
        elif X <= compare_U and compare_X <= U and Y >= compare_V and compare_Y >= V:
            if X > compare_X:
                compare_X = X
            if Y < compare_Y:
                compare_Y = Y
            if U < compare_U:
                compare_U = U
            if V > compare_V:
                compare_V = V
        else:
            valid = False

    print("Teste " + str(counter))
    if valid:
        print(f'{compare_X} {compare_Y} {compare_U} {compare_V}')
    else:
        print('nenhum')
    print('')
    N = int(input())
    counter += 1
