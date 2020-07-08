O = input()

M = [[] for x in range(12)]

for i in range(12):
    for z in range(12):
        M[i].append(float(input()))

sumTotal = 0

for i in range(5):
    sumTotal += sum(M[i][i + 1: -1 * i - 1])

if O == 'S':
    print(round(sumTotal, 1))
else:
    print(round(sumTotal/30, 1))
