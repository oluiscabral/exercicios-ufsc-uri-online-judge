while True:
    try:
        N, M = [int(w) for w in input().split()]

        pL = -1
        pC = -1
        aL = -1
        aC = -1
        repCounter = 0
        city = []
        for i in range(N):
            city.append([int(w) for w in input().split()])

        hasPlayer = False
        hasA = False
        for l in range(N):
            for c in range(M):
                if city[l][c] == 2:
                    hasA = True
                    aL = l
                    aC = c
                elif city[l][c] == 1:
                    hasPlayer = True
                    pL = l
                    pC = c
                if hasA and hasPlayer:
                    break

        while pL != aL:
            if pL < aL:
                pL += 1
            else:
                pL -= 1
            repCounter += 1

        while pC != aC:
            if pC < aC:
                pC += 1
            else:
                pC -= 1
            repCounter += 1

        print(repCounter)

    except EOFError:
        break
