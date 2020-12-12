# pega o número de salas
N = int(input())

# cria uma lista com a quantidade de vidas em cada sala por meio da sintaxe de list comprehension
lifes = [int(w) for w in input().split()]

# inicializa as variáveis para comparar os valores em sequencia
maximum = 0
compare = 0

# pega número a número da lista
for n in lifes:
    # pega apenas valores >= 0
    compare = max(0, compare + n)
    # pega o maior valor, comparando o valor atual com o máximo armazenado
    maximum = max(compare, maximum)

# apresenta na tela o valor máximo possível
print(maximum)
