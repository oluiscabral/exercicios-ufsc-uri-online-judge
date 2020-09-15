N = int(input())

t = 1
while N != 0:
    value = 1
    for i in range(N-1):
        value = value * 2 + 1
    output = "Teste " + str(t) + "\n" + str(value) + "\n"
    print(output)
    t += 1
    N = int(input())
