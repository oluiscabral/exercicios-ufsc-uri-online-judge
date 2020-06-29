P, N, C = [int(x) for x in input().split()]

while P != 0 or N != 0 or C != 0:

    sequence = []
    for i in range(N):
        sequence.append([int(x) for x in input().split()])

    counter = 0
    for i in range(P):
        streak = 0
        for z in range(N):
            if sequence[z][i] == 1:
                streak += 1
                if z == N-1 and streak >= C:
                    counter += 1
            else:
                if streak >= C:
                    counter += 1
                streak = 0

    print(counter)

    P, N, C = [int(x) for x in input().split()]
