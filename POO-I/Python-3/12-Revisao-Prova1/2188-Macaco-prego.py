N = int(input())

counter = 1
last_ret = {}
intersec_X = -1
intersec_Y = -1
intersec_U = -1
intersec_V = -1

while N != 0:
    has_ret_values = False
    has_intersec_values = False

    valid = True
    for i in range(N):
        X, Y, U, V = [int(w) for w in input().split()]

        if not has_ret_values:
            last_ret = {
                'X': X,
                'Y': Y,
                'U': U,
                'V': V
            }
            has_ret_values = True
            continue
        elif (X < last_ret['U'] and Y > last_ret['V']) or (last_ret['X'] < U and last_ret['Y'] > V):
            last_ret = {
                'X': X,
                'Y': Y,
                'U': U,
                'V': V
            }
            if has_intersec_values:
                compare_X = intersec_X
                compare_Y = intersec_Y
                compare_U = intersec_U
                compare_V = intersec_V
            else:
                compare_X = last_ret['X']
                compare_Y = last_ret['Y']
                compare_U = last_ret['U']
                compare_V = last_ret['V']
                has_intersec_values = True
            greater_X = X
            smaller_Y = Y
            smaller_U = U
            greater_V = V
            if X < compare_X:
                greater_X = compare_X
            if Y > compare_Y:
                smaller_Y = compare_Y
            if U > compare_U:
                smaller_U = compare_U
            if V < compare_V:
                greater_V = compare_V
            intersec_X = greater_X
            intersec_Y = smaller_Y
            intersec_U = smaller_U
            intersec_V = greater_V
        else:
            valid = False

    print("Teste " + str(counter))
    if valid:
        print(f'{intersec_X} {intersec_Y} {intersec_U} {intersec_V}')
    else:
        print('nenhum')
    print('')
    N = int(input())
    counter += 1
