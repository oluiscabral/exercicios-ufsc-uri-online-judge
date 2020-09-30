N, C = [int(w) for w in input().split()]

total = 0
excedeed = False

for i in range(N):
    S, E = [int(w) for w in input().split()]
    total = total - S + E
    if not excedeed and total > C:
        excedeed = True

if excedeed:
    print('S')
else:
    print('N')
