X = int(input())

counter = 0
i = 0
while True:
    n = X + i
    if n % 2 != 0:
        print(n)
        counter += 1
    i += 1
    if counter == 6:
        break
