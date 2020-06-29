N = int(input())

l = 0
r = 0
cells = []
mines = [int(0) for i in range(N)]

for i in range(N):
    cells.append(int(input()))

for i in range(N):
    l = i - 1
    r = i + 1

    if cells[i]:
        mines[i] += 1

    if l >= 0:
        if cells[l]:
            mines[i] += 1
    if r < N:
        if cells[r]:
            mines[i] += 1

for mine in mines:
    print(mine)
