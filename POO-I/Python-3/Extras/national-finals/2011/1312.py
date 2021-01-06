while True:
    N = int(input())
    if N == 0:
        break
    greatest = 0
    stack = [[0 for i in range(N + 2)] for j in range(N + 2)]
    for i in range(N):
        stack[i+1][-1] = 0
        for j, value in enumerate([int(w) for w in input().split()]):
            x = i-j+1
            stack[x][j+1] = value + stack[x][j] + stack[x-1][j+1] - stack[x-1][j]
            greatest = max(greatest, stack[x][j+1])
    for i in range(N):
        for j in range(N-i, 0, -1):
            current = stack[i+1][j] - stack[i+1][j-1]
            greatest = max(greatest, stack[i+1][j] + stack[i][j+1])
            stack[i+1][j] = max(max(stack[i][j+1] + current, current),
                                max(stack[i+1][j+1] + current, stack[i][j]))
    print(greatest)
