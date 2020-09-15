initial = (0, 0)
final = (4, 4)
N = 5


def getPossibilities(position):
    global N, grid
    l, c = position
    possibilities = []
    # left, down, right, top
    directions = [[l, c - 1], [l+1, c], [l, c + 1], [l-1, c]]
    for d in directions:
        dL, dC = d[0], d[1]
        if dL >= 0 and dL < N and dC >= 0 and dC < N and grid[dL][dC] == True:
            possibilities.append((dL, dC))
    return possibilities


def mark(initial):
    global grid, connections
    if not grid[initial[0]][initial[1]]:
        return False
    grid[initial[0]][initial[1]] = False
    connections.append(initial)
    for pos in graphs[initial]:
        mark((pos[0], pos[1]))
    return True


T = int(input())
for i in range(T):
    grid = []
    for i in range(N):
        inp = input()
        while inp == '':
            inp = input()
        line = [(w == '0') for w in inp.split()]
        grid.append(line)

    graphs = {}
    for i in range(N):
        for j in range(N):
            position = (i, j)
            graphs[position] = getPossibilities(position)

    connections = []

    mark(initial)  # recursion init
    if final in connections:
        print('COPS')
    else:
        print('ROBBERS')
