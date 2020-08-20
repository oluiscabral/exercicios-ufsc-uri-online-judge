V, N, M = input().split()
while V != '0' or N != '0' or M != '0':
    if len(N) < 4:
        N = N.rjust(4, '0')
    if len(M) < 4:
        M = M.rjust(4, '0')

    streak = 0
    for i in range(-1, len(N)*-1-1, -1):
        try:
            if streak < 4 and N[i] == M[i]:
                streak += 1
            else:
                break
        except:
            break

    prize = 0
    if streak == 4:
        prize = float(V) * 3000
    elif streak == 3:
        prize = float(V) * 500
    elif streak == 2:
        prize = float(V) * 50
    else:
        init = 97
        limit = 100
        n = int(N[-2:])
        if n != 0 and n < init:
            init = 93
            limit = 97
            if n < init:
                keys = [w for w in range(1, 95, 4)]
                for i in range(len(keys)-1):
                    if n >= keys[i] and n < keys[i+1]:
                        init = keys[i]
                        limit = keys[i+1]
                        break
        m = int(M[-2:])
        if m == 0:
            m = 100
        if m >= init and m < limit:
            prize = float(V) * 16

    print("{0:.2f}".format(prize))

    V, N, M = input().split()
