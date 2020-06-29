N = int(input())

while N != 0:
    H = [int(x) for x in input().split()]

    peakCount = 0
    ascending = False

    if H[0] > H[N - 1]:
        ascending = True

    for i in range(-N+1, 1):
        if not ascending and H[i] > H[i-1]:
            ascending = True
            peakCount += 1
        elif ascending and H[i] < H[i-1]:
            ascending = False
            peakCount += 1

    print(peakCount)
    N = int(input())
