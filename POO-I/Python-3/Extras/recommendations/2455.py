P1, C1, P2, C2 = [int(w) for w in input().split()]

left = P1 * C1
right = P2 * C2

if left == right:
    print(0)
elif left > right:
    print(-1)
else:
    print(1)
