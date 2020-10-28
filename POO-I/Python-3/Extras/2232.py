T = int(input())

for i in range(T):
    N = int(input())
    total = 0
    for j in range(N):
        total += 2**j
    print(total)
