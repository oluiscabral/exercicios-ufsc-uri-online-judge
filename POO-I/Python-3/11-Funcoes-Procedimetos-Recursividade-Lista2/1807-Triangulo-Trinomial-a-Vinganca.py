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


R = int(input())
result = fastPower(3, R)

print(result)
