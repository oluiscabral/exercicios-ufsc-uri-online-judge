# pega o valor de entrada
N = int(input())

# inicia a variável que será a matriz
K = []
for i in range(N):
    # adiciona uma linha a matriz, com os valores de entrada
    K.append([int(w) for w in input().split()])

# define uma lista não ordenada para armazenar as especies já capturadas
collected = set()
# loop para pegar as posições de captura
for i in range(2 * N):
    # pega as posições de busca na matriz
    x, y = [int(w) - 1 for w in input().split()]
    # pega o valor da espécie
    specie = K[x][y]
    # verifica se a especie não está na lista de coletadas
    if specie not in collected:
        collected.add(specie)

print(len(collected))
