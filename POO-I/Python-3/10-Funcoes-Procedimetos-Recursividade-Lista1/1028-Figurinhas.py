def mcd(n1, n2):
    a = n1
    b = n2
    remainder = -1
    while remainder != 0:
        remainder = a % b
        a  = b
        b  = remainder
    return a

for i in range(int(input())):
    F1, F2 = [int(w) for w in input().split()]
    print(mcd(F1, F2))
