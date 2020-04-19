A, B, C = [int(x) for x in input().split()]

campeao = max([A,B,C])
ultimo = min([A,B,C])
vice = A + B + C - campeao - ultimo

print(vice)