C = int(input())


def getDestroyedWall(M, N, wall, l, c):
    virtualWall = [[0 for x in range(N)] for w in range(M)]
    virtualWall[l][c] = 10

    adder = 9
    r = 2
    for h in range(l+1, M):
        virtualWall[h][c] = adder
        dC = c - 1
        while dC >= 0 and dC > c - r:
            virtualWall[h][dC] = adder
            dC -= 1
        dC = c + 1
        while dC < N and dC < c + r:
            virtualWall[h][dC] = adder
            dC += 1
        if adder > 1:
            adder -= 1
        r += 1

    adder = 9
    r = 2
    for h in range(l-1, -1, -1):
        virtualWall[h][c] = adder
        dC = c - 1
        while dC >= 0 and dC > c - r:
            virtualWall[h][dC] = adder
            dC -= 1
        dC = c + 1
        while dC < N and dC < c + r:
            virtualWall[h][dC] = adder
            dC += 1
        if adder > 1:
            adder -= 1
        r += 1
    # --- // --- #
    adder = 9
    r = 2
    for v in range(c+1, N):
        virtualWall[l][v] = adder
        dL = l - 1
        while dL >= 0 and dL > l - r:
            virtualWall[dL][v] = adder
            dL -= 1
        dL = l + 1
        while dL < M and dL < l + r:
            virtualWall[dL][v] = adder
            dL += 1
        if adder > 1:
            adder -= 1
        r += 1

    adder = 9
    r = 2
    for v in range(c - 1, -1, -1):
        virtualWall[l][v] = adder
        dL = l - 1
        while dL >= 0 and dL > l - r:
            virtualWall[dL][v] = adder
            dL -= 1
        dL = l + 1
        while dL < M and dL < l + r:
            virtualWall[dL][v] = adder
            dL += 1
        if adder > 1:
            adder -= 1
        r += 1

    for l in range(M):
        for c in range(N):
            wall[l][c] += virtualWall[l][c]
    return wall


for i in range(C):
    M, N, X, Y = [int(w) for w in input().split()]

    initialWall = []
    for k in range(M):
        initialWall.append([int(w) for w in input().split()])

    printable = ""
    afterPunchWall = getDestroyedWall(M, N, initialWall, X - 1, Y - 1)

    for line in afterPunchWall:
        for cell in line:
            printable += str(cell) + " "
        printable = printable[:-1] + "\n"

    printable = printable.rstrip()

    print("Parede " + str(i+1) + ":")
    print(printable)
