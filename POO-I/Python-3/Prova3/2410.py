# pega o número total de registros
N = int(input())

# inicializa uma lista sem ordem para conter todos os registros sem repetição
V = set()
# variável para contar quantos não se repetiram
counter = 0
# itera de 0 a N-1
for i in range(N):
    # pega o número de registro
    entry = int(input())
    # verifica se o número de registro não está contido na lista
    if entry not in V:
        # não está, portanto adiciona ele
        V.add(entry)
        # adiciona mais um no total dos que não se repetiram
        counter += 1

# apresenta o tamanho da lista
print(counter)
