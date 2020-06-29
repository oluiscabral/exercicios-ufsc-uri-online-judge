N = int(input())

while N != 0:

    pairs = 0
    for i in range(N):
        C, V = [int(x) for x in input().split()]
        pairs += V // 2

    print(pairs//2)

    N = int(input())
