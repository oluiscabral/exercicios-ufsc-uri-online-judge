def mcd(n1, n2):
    # função que pega o máximo divisor comum entre 2 números
    a = n1
    b = n2
    remainder = -1
    while remainder != 0:
        remainder = a % b
        a = b
        b = remainder
    return a


def lcm(numbers):
    # função que pega o mmc de uma lista de números
    lcm = numbers[0]
    for i in range(1, len(numbers)):
        lcm = lcm*numbers[i]//mcd(lcm, numbers[i])
    return lcm


while True:
    try:
        # pega o valor de entrada
        M = int(input())
        # pega os tempos de ciclo
        L = [int(w) for w in input().split()]
        # o resultado é o mmc dos 3 números - o tempo do último alinhamento
        r = lcm(L) - M
        print(r)
    except EOFError:
        break
