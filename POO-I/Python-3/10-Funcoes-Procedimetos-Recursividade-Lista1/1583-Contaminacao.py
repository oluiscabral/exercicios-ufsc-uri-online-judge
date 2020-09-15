def infectVertical(grid):
    global N, M
    for i in range(M):
        infecting = False
        for j in range(N):
            c = grid[j][i]
            if c == 'T':
                infecting = True
                continue
            if c == 'A':
                if infecting:
                    grid[j][i] = 'T'
            else:
                infecting = False
    for i in range(M):
        infecting = False
        for j in range(N-1, -1, -1):
            c = grid[j][i]
            if c == 'T':
                infecting = True
                continue
            if c == 'A':
                if infecting:
                    grid[j][i] = 'T'
            else:
                infecting = False


def infectHorizontal(grid):
    global N, M
    for i in range(N):
        infecting = False
        for j in range(M):
            c = grid[i][j]
            if c == 'T':
                infecting = True
                continue
            if c == 'A':
                if infecting:
                    grid[i][j] = 'T'
            else:
                infecting = False
    for i in range(N):
        infecting = False
        for j in range(M-1, -1, -1):
            c = grid[i][j]
            if c == 'T':
                infecting = True
                continue
            if c == 'A':
                if infecting:
                    grid[i][j] = 'T'
            else:
                infecting = False


def copy(grid):
    vGrid = []
    for line in grid:
        vGrid.append(line.copy())
    return vGrid


def infect(grid):
    vGrid = copy(grid)
    while True:
        # horizontal
        infectHorizontal(grid)
        # vertical
        infectVertical(grid)
        if vGrid != grid:
            vGrid = copy(grid)
        else:
            break
    return grid


N, M = [int(w) for w in input().split()]

while N != 0 or M != 0:
    grid = []
    for i in range(N):
        grid.append(list(input()))
    grid = infect(grid)
    for i in range(N):
        output = "".join([c for c in grid[i]])
        print(output)
    print('')
    N, M = [int(w) for w in input().split()]
