N, M = [int(x) for x in input().split()]
stones = [0 for i in range(N)]

frogs = []
for i in range(M):
    P, D = [int(x) for x in input().split()]
    frogs.append([P-1, D])

for frog in frogs:
    if all(stones):
        break

    frogPos = frog[0]
    frogJump = frog[1]

    forwardable = True
    backwardable = True
    forwardPossibility = 0
    backwardPossibility = 0
    i = 1

    stones[frogPos] = 1

    while forwardable or backwardable:
        forwardPossibility = frogPos + frogJump*i
        backwardPossibility = frogPos - frogJump*i

        if forwardable and forwardPossibility < N:
            stones[forwardPossibility] = 1
        else:
            forwardable = False

        if backwardable and backwardPossibility >= 0:
            stones[backwardPossibility] = 1
        else:
            backwardable = False

        if all(stones):
            break

        i += 1

for stone in stones:
    print(stone)
