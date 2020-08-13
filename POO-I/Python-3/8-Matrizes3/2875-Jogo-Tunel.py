# left: [left, down, right, top],
# down: [left, down, right, top],
# right: ...,
# top: ...
directionsDict = {
    0: ["F", "L", "X", "R"],
    1: ["R", "F", "L", "X"],
    2: ["X", "R", "F", "L"],
    3: ["L", "X", "R", "F"]
}


def nextValidPos(l, c, d):
    global lastL, lastC

   # left, down, right, top
    directions = [[l, c - 1], [l + 1, c], [l, c + 1], [l - 1, c]]
    for i in range(4):
        dL, dC = directions[i][0], directions[i][1]
        dRep = directionsDict[d][i]
        if dL >= 0 and dL < N and dC >= 0 and dC < M and (dL != lastL or dC != lastC) and track[dL][dC] == '0':
            if dRep == "F":
                lastL = l
                lastC = c
                return [dL, dC, i], dRep
            else:
                return [l, c, i], dRep

    return None, "E"


while True:
    try:
        N, M = [int(w) for w in input().split()]
        track = [[w for w in input().split()] for z in range(N)]
        # position is 0-based
        stat = [0, track[0].index("X"), 1]

        lastL, lastC = stat[0], stat[1]
        result = ""
        while True:
            nextStat, dRep = nextValidPos(stat[0], stat[1], stat[2])
            result += dRep + " "
            if nextStat != None:
                stat = nextStat
            else:
                break
        result = result[:-1]
        print(result)
    except EOFError:
        break
