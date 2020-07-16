N, M = [int(x) for x in input().split()]
consistentPlayers = 0
for i in range(N):
    if all([int(x) for x in input().split()]):
        consistentPlayers += 1
print(consistentPlayers)
