L = int(input())
T = input()
M = [[] for x in range(12)]

for i in range(12):
    for z in range(12):
        M[i].append(float(input()))

sumTotal = sum(M[L])
if T == 'S':
    print(sumTotal)
else:
    print(round(sumTotal/12, 1))
