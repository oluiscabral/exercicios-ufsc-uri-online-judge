N, M = [int(w) for w in input().split()]

# get all the ground cells -> ground[line][column]
ground = [[int(w) for w in input().split()] for z in range(N)]

greatestLineSum = 0
greatestColumnSum = 0

# check for the greatest line sum
for line in ground:
    lineSum = sum(line)
    if lineSum > greatestLineSum:
        greatestLineSum = lineSum

# check for the greatest column sum
for i in range(M):
    columnSum = 0
    for j in range(N):
        columnSum += ground[j][i]
    if columnSum > greatestColumnSum:
        greatestColumnSum = columnSum

if greatestLineSum > greatestColumnSum:
    print(greatestLineSum)
else:
    print(greatestColumnSum)
