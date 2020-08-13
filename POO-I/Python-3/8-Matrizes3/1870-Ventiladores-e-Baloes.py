def getNearestFansSum(l, p):
    global path
    # considering that it is not a fan location
    leftFan = 0
    rightFan = 0
    w = p-1
    while w >= 0 and path[l][w] == 0:
        w -= 1
    if w >= 0:
        leftFan = path[l][w]
    w = p+1
    while w < C and path[l][w] == 0:
        w += 1
    if w < C:
        rightFan = path[l][w]
    return leftFan - rightFan


L, C, P = [int(x) for x in input().split()]
while L != 0 or C != 0 or P != 0:
    path = []
    for i in range(L):
        path.append([int(x) for x in input().split()])

    p = P-1
    boomed = False
    for i in range(L):
        if path[i][p] == 0:
            p += getNearestFansSum(i, p)
            if p <= 0 or p >= C - 1:
                # in this case, p got out of bounds on the line, so we gotta break it right here
                boomed = True
                break
        else:
            boomed = True
            break

    if boomed:
        print("BOOM " + str(i+1) + " " + str(p+1))
    else:
        print("OUT " + str(p + 1))

    L, C, P = [int(x) for x in input().split()]
