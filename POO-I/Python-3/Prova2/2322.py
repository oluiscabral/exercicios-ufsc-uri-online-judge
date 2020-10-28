# pega a quantidade de números que a sequência terá
N = int(input())

# instancia uma lista pela sintaxe de list comprehension dos valores da sequência (valores do input() separados por espaço)
sequence = [int(w) for w in input().split()]

# loop que conta de 1 até N+1
for i in range(1, N + 1):
    # verifica se i (o número atual da contagem) não está dentro da lista da sequência
    if not sequence.__contains__(i):
        # i não está dentro da lista de sequência, então apresenta ele na tela
        print(i)
        # quebra (para) o loop
        break
