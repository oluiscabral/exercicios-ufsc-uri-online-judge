N, K = [int(w) for w in input().split()]

# I'm sorry for the amount of hard code :)


def getDestinations(x, y, d):
    global N
    focals = {
        'top': [x, y - d],
        'bot': [x, y + d],
        'right': [x + d, y],
        'left': [x-d, y]
    }

    destinations = []

    # go from top to the right and left focals
    pos = focals['top'].copy()
    while pos[0] <= focals['right'][0] and pos[1] <= focals['right'][1]:
        if pos[0] >= 0 and pos[0] < N and pos[1] >= 0 and pos[0] < N:
            destinations.append(pos.copy())
        pos[0] += 1
        pos[1] += 1

    pos = focals['top'].copy()
    pos[0] -= 1
    pos[1] += 1
    while pos[0] >= focals['left'][0] and pos[1] <= focals['left'][1]:
        if pos[0] >= 0 and pos[0] < N and pos[1] >= 0 and pos[0] < N:
            destinations.append(pos.copy())
        pos[0] -= 1
        pos[1] += 1

    pos = focals['bot'].copy()
    while pos[0] < focals['right'][0] and pos[1] > focals['right'][1]:
        if pos[0] >= 0 and pos[0] < N and pos[1] >= 0 and pos[0] < N:
            destinations.append(pos.copy())
        pos[0] += 1
        pos[1] -= 1

    pos = focals['bot'].copy()
    pos[0] -= 1
    pos[1] -= 1
    while pos[0] > focals['left'][0] and pos[1] > focals['left'][1]:
        if pos[0] >= 0 and pos[0] < N and pos[1] >= 0 and pos[0] < N:
            destinations.append(pos.copy())
        pos[0] -= 1
        pos[1] -= 1

    return destinations


# get all move destination possibilities from the tips position
lastDestinations = None
isValid = True
for i in range(K):
    X, Y, D = [int(w) for w in input().split()]
    if isValid:
        destinations = getDestinations(X, Y, D)
        intersection = []
        if lastDestinations == None:
            lastDestinations = destinations
        else:
            lastDestinations = [
                value for value in destinations if value in lastDestinations
            ]

        if len(lastDestinations) == 0:
            isValid = False

if isValid and len(lastDestinations) == 1:
    X, Y = lastDestinations[0]
    print(str(X) + ' ' + str(Y))
else:
    print('-1 -1')
