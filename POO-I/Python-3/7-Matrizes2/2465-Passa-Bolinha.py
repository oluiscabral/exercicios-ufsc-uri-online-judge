N = int(input())

initialPos = [int(w)-1 for w in input().split()]

yard = []
flags = 0

for i in range(N):
    yard.append([
        [int(w), 0, False] for w in input().split()
    ])


def rotateAndPass(x, y):
    global flags
    flags += 1
    yard[x][y][2] = True
    directions = [[x, y - 1], (x+1, y), (x, y + 1), (x-1, y)]
    for d in directions:
        dX, dY = d[0], d[1]
        if dX >= 0 and dX < N and dY >= 0 and dY < N and yard[dX][dY][0] >= yard[x][y][0] and not yard[dX][dY][2]:
            rotateAndPass(dX, dY)


rotateAndPass(initialPos[0], initialPos[1])

print(flags)
