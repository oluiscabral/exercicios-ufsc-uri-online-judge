def mcd(n1, n2):
    a = n1
    b = n2
    remainder = -1
    while remainder != 0:
        remainder = a % b
        a = b
        b = remainder
    return a


def lcm(a):
    lcm = a[0]
    for i in range(1, len(a)):
        lcm = lcm*a[i]//mcd(lcm, a[i])
    return lcm


N = int(input())

holes = []
holes.extend([(int(w)-1) for w in input().split()])

test = [False]*N
frequencies = []
while not all(test):
    initial = test.index(False)

    freq = 1
    destination = holes[initial]
    test[destination] = True
    while initial != destination:
        destination = holes[destination]
        test[destination] = True
        freq += 1
    frequencies.append(freq)

r = frequencies[0]
if len(frequencies) > 1:
    r = lcm(frequencies)

print(r)
