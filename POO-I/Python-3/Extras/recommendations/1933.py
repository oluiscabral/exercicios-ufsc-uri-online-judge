A, B = [int(w) for w in input().split()]

best = A
if B > A:
    best = B

print(best)
