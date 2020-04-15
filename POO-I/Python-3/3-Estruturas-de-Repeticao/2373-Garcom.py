N = int(input())

copos_quebrados = 0

for i in range(N):
    L, C = [int(x) for x in input().split()]

    if L > C:
        copos_quebrados += C

print(copos_quebrados)