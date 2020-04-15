N = int(input())

n = 1
while N != -1:

    dobras = (2**N + 1)**2

    print("Teste "+ str(n))
    print(dobras)
    print("")

    n += 1

    N = int(input())