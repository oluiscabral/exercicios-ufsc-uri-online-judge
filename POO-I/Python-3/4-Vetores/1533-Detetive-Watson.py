N = int(input())

while N != 0:

    suspects = [int(x) for x in input().split()]

    mostSuspect = max(suspects)

    assassin = -1
    for s in suspects:
        if s < mostSuspect and s > assassin:
            assassin = s

    print(suspects.index(assassin)+1)

    N = int(input())
