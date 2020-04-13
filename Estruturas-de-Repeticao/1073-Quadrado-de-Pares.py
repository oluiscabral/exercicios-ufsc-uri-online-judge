N = int(input())

i = int(1)

while i <= N:
    if (i % 2) == 0:
        print(str(i) + "^2 = " + str(i**2))
    i += 1