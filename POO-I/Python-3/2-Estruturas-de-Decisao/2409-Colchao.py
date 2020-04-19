A, B, C = [int(x) for x in input().split()]

H, L = [int(x) for x in input().split()]

if (A <= L and B <= H) or (A <= H and B <= L):
    print("S")
elif (A <= L and C <= H) or (A <= H and C <= L):
    print("S")
elif (B <= L and C <= H) or (B <= H and C <= L):
    print("S")
else:
    print("N")