O = input()

M = [[] for x in range(12)]

for i in range(12):
    for z in range(12):
        M[i].append(float(input()))

divisor = 0
sumTotal = 0

for i in range(1, 6):
    sumTotal += sum(M[i][-1:(i*-1)-1:-1])
    divisor += i

for i in range(10, 5, -1):
    sumTotal += sum(M[i][-1:i-12:-1])
    divisor += 11 - i

if O == 'S':
    print(sumTotal)
else:
    print(round(sumTotal/divisor, 1))
