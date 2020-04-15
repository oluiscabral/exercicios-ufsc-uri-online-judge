N = int(input())

n = 1
while N != 0:

    diferenca = 0

    print("Teste "+ str(n))

    for i in range(N):
        J, Z = [int(x) for x in input().split()]

        diferenca += J - Z

        print(diferenca)

    print("")
    n += 1
    N = int(input())