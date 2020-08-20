N = int(input())

while N != 0:
    numbers = {}
    for w in input().split():
        if numbers.get(w, False):
            numbers[w] += 1
        else:
            numbers.update({w: 1})

    for key in numbers.keys():
        value = numbers.get(key)
        if value % 2 != 0:
            alone = key
            break

    print(key)

    N = int(input())
