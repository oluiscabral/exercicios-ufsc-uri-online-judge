N, K = [int(x) for x in input().split()]

h = [int(x) for x in input().split()]

beautiful = True
peakCounter = 0
valleyCounter = 0

i = 1
while i in range(1, N-1):
    if h[i] > h[i - 1] and h[i] > h[i + 1]:
        peakCounter += 1
        i += 2
    else:
        i += 1

if peakCounter == K:
    i = 2
    while i in range(2, N - 2):
        if h[i] < h[i - 1] and h[i] < h[i + 1]:
            valleyCounter += 1
            i += 2
        else:
            i += 1
    if valleyCounter != K - 1:
        beautiful = False
else:
    beautiful = False

if beautiful:
    print("beautiful")
else:
    print("ugly")
