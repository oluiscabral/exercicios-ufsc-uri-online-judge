N, M = [int(x) for x in input().split()]

P = [int(x) for x in input().split()]
P.append(42195)

v = True
stopPoint = 0 + M
for i in range(1, N+1):
    if stopPoint >= P[i]:
        stopPoint = P[i] + M
    else:
        v = False
        break

print('S') if v else print('N')
