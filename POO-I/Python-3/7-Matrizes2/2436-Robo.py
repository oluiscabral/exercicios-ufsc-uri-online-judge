# Lines and columns
L, C = [int(x) for x in input().split()]

# Initial coordinates
A, B = [int(x)-1 for x in input().split()]

# each line is an array with C columns
# tileColors[0][0] is equal to tileColors from line 1 and column 1
tileColors = []
robotL = A
robotC = B

for i in range(L):
    tileColors.append([int(x) for x in input().split()])


def nextValidPos(l, c, lastL, lastC):
    # left, down, right, top
    directions = [[l, c - 1], [l+1, c], [l, c + 1], [l-1, c]]
    for d in directions:
        dL, dC = d[0], d[1]
        if dL >= 0 and dL < L and dC >= 0 and dC < C and (dL != lastL or dC != lastC) and tileColors[dL][dC] == 1:
            return [dL, dC]

    return None


lastL = A
lastC = B
while True:
    nextPos = nextValidPos(robotL, robotC, lastL, lastC)
    if nextPos != None:
        lastL = robotL
        lastC = robotC
        robotL, robotC = nextPos
    else:
        break

print(str(robotL+1) + " " + str(robotC+1))
