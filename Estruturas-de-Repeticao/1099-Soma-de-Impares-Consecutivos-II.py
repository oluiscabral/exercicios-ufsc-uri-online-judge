N = int(input())

for i in range(0, N):
    X,Y = [int(z) for z in input().split()]

    if X > Y:
        C = Y
        F = X
    else:
        C = X
        F = Y
    
    soma = int(0)
    for k in range(C+1,F):
        if k % 2 != 0:
            soma += k
    print(soma)