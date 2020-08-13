N = int(input())

square = [[int(w) for w in input().split()] for z in range(N)]

# let's compare all the other lines using the first one
firstLineSum = sum(square[0])

correctSum = firstLineSum
wrongSum = 0

diffLine = -1

hadEquals = False
hadDiff = False

for i in range(1, N):
    lineSum = sum(square[i])

    if lineSum != firstLineSum:
        if hadDiff:
            # the wrong line actually is the first one
            diffLine = 0
            wrongSum = firstLineSum
            correctSum = lineSum
            break
        hadDiff = True
        diffLine = i
        wrongSum = lineSum
        continue

    hadEquals = True
    if hadDiff and hadEquals:
        # if we already caught a diff and got lines that are equals, there is no reason to go further in this loop
        break

# now lets check for the wrong column using some of the values we got
diffColumn = -1
for i in range(N):
    columnSum = 0
    for j in range(N):
        columnSum += square[j][i]

    if columnSum != correctSum:
        diffColumn = i
        break

# the wrong number is:
wrongNumber = square[diffLine][diffColumn]

# and the correct (original) number is:
sumDiff = correctSum - wrongSum
correctNumber = wrongNumber + sumDiff

print(str(correctNumber) + " " + str(wrongNumber))
