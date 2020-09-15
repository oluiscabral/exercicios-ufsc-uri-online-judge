def mcd(n1, n2):
    a = n1
    b = n2
    remainder = -1
    while remainder != 0:
        remainder = a % b
        a = b
        b = remainder
    return a


def irreducible(n1, n2):
    v = mcd(n1, n2)
    n1, n2 = n1 / v, n2 / v
    return int(n1), int(n2)


a, b, c, d = [int(w) for w in input().split()]

if b != d:
    n1, n2 = irreducible(a * d + c * b, b * d)
else:
    n1, n2 = irreducible(a + c, b)

print(str(n1) + " " + str(n2))
