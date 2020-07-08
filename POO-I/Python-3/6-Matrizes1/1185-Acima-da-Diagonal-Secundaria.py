O = input()

M = [[] for x in range(12)]

for i in range(12):
    for z in range(12):
        M[i].append(float(input()))

divisor = 0
sumTotal = 0

for i in range(11):
    sumTotal += sum(M[i][0: -1 - i])
    divisor += i+1

if O == 'S':
    print(sumTotal)
else:
    print(round(sumTotal/divisor, 1))
