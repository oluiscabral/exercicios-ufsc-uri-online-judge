V = int(input())

n = 1
while V != 0:
    I, J, K, L = 0, 0, 0 ,0

    resto = V
    I = resto // 50
    resto -= I * 50
    
    J = resto // 10
    resto -= J * 10

    K = resto // 5
    resto -= K * 5

    L = resto

    print("Teste "+ str(n))
    print(str(I) + " " + str(J) + " " + str(K) + " " + str(L))
    print("")

    n += 1

    V = int(input())