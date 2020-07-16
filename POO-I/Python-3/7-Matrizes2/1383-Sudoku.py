for i in range(int(input())):
    isValid = True
    board = [[int(w) for w in input().split()] for z in range(9)]
    regions = [[] for w in range(9)]
    j, k, l, m = 0, 0, 0, 0
    for line in board:
        k = 0
        for value in line:
            regions[k+3*m].append(value)
            j += 1
            if j == 3:
                k += 1
                j = 0
        l += 1
        if l == 3:
            m += 1
            l = 0
    for region in regions:
        for value in region:
            if region.count(value) > 1:
                isValid = False
    if isValid:
        for line in board:
            for value in line:
                if line.count(value) > 1:
                    isValid = False
                    break
            if not isValid:
                break
        if isValid:
            for j in range(9):
                for k in range(9):
                    for l in range(k+1, 9):
                        if board[k][j] == board[l][j]:
                            isValid = False
                            break
                if not isValid:
                    break
    print("Instancia " + str(i + 1))
    if isValid:
        print("SIM")
    else:
        print("NAO")
    print("")
