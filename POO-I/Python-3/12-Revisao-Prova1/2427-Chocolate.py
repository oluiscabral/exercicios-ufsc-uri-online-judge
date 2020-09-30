def fastPower(base, exp):
    mod = 2**31 - 1
    if exp == 0:
        x = 1
    else:
        half = fastPower(base, exp // 2)  # just / in Python 2
        x = half * half
        if exp % 2 == 1:
            x *= base
    return x % mod


L = int(input())

counter = 0
d = L
while d > 1:
    d = d // 2
    counter += 1

if L > 0:
    print(str(fastPower(4, counter)))
