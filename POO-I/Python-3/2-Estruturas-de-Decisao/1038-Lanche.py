C, Q = [int(x) for x in input().split()]

if C == 1:
    total = 4 * Q
elif C == 2:
    total = 4.5 * Q
elif C == 3:
    total = 5 * Q
elif C == 4:
    total = 2 * Q
else:
    total = 1.5 * Q

print("Total: R$ {0:.2f}".format(total))