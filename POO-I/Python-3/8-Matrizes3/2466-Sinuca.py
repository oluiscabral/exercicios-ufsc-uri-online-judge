N = int(input())

compareRow = [int(x) for x in input().split()]
i = N
while i > 1:
    nextRow = []
    for j in range(0, i - 1):
        if compareRow[j] == compareRow[j + 1]:
            nextRow.append(1)
        else:
            nextRow.append(-1)
    compareRow = nextRow
    i -= 1

if compareRow[0] == 1:
    print("preta")
else:
    print("branca")
