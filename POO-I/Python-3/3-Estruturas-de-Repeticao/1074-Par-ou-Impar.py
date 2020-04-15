N = int(input())

i = int(1)

X = []

while i <= N:
    X.append(int(input()))
    i += 1

for z in X:
    if z == 0:
        print("NULL")
    else:
        if (z % 2) == 0:
            print("EVEN", end=" ")
        else:
            print("ODD", end=" ")
        if z > 0:
            print("POSITIVE")
        else:
            print("NEGATIVE")