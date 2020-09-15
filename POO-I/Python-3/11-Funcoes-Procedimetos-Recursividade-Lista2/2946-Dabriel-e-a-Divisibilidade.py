N = int(input(), 2)
M = int(input())

divisibles = []
hasDivisible = False
for i in range(M):
    v = int(input())
    if N % v == 0:
        divisibles.append(v)
        hasDivisible = True

if hasDivisible:
    divisibles.sort()
    output = ""
    for n in divisibles:
        output += str(n) + ' '
    output = output[:-1]
    print(output)
else:
    print('Nenhum')
