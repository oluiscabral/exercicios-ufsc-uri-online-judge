def mcd(n1, n2):
    a = n1
    b = n2
    remainder = -1
    while remainder != 0:
        remainder = a % b
        a = b
        b = remainder
    return a


while True:
    try:
        inp = [int(w) for w in input().split()]
        inp.sort()
        a, b, c = inp
        primitive = False

        triple = c ** 2 == a ** 2 + b ** 2
        if triple:
            primitive = mcd(mcd(a, b), c) == 1

        if triple and primitive:
            print("tripla pitagorica primitiva")
        elif triple:
            print("tripla pitagorica")
        else:
            print("tripla")
    except EOFError:
        break
