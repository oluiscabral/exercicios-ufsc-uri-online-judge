L, A, P, R = [int(x) for x in input().split()]

if ((L/2)**2 + (P/2)**2 + (A/2)**2) <= R**2:
    print("S")
else:
    print("N")