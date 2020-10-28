N = int(input())

initial = 65

for i in range(N):
    total = 0
    L = int(input())
    for j in range(L):
        inp = input()
        for k in range(len(inp)):
            total += k + j
            total += ord(inp[k]) - initial
    print(total)
