def checkAround(l, c):
    global N, M, breadBoard
    internalCounter = 0
    # left, down, right, top
    directions = [[l, c - 1], [l+1, c], [l, c + 1], [l-1, c]]
    for d in directions:
        dL, dC = d[0], d[1]
        if dL >= 0 and dL < N and dC >= 0 and dC < M and breadBoard[dL][dC] == 1:
            internalCounter += 1

    return internalCounter


while True:
    try:
        N, M = [int(w) for w in input().split()]

        breadBoard = []
        printable = ""
        for i in range(N):
            breadBoard.append([int(w) for w in input().split()])

        for line in range(N):
            for column in range(M):
                if breadBoard[line][column] == 0:
                    printable += str(checkAround(line, column))
                else:
                    printable += "9"
            printable += "\n"

        printable = printable.rstrip()

        print(printable)

    except EOFError:
        break
