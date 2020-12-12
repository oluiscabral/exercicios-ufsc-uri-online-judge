# pega o número de instâncias
T = int(input())

# itera T vezes
for i in range(T):
    if i:
        # pula uma linha entre cada instância
        print()

    # pega a entrada de números na mesma linha separados por espaço
    N, L = [int(w) for w in input().split()]

    # cria um dicionário para armazenar a soma total de cada posição da matriz
    position_sums = {}
    # itera L vezes
    for j in range(L):
        # pega 4 valores da entrada separados por espaço
        p, l, c, v = [int(w) for w in input().split()]
        # define uma tupla da posição da matriz
        pos = (l, c)
        # verifica se a tupla já existe no dicionário criado
        if pos in position_sums:
            # existe, portanto soma o valor da posição
            position_sums[pos] += v
        else:
            # não existe, portanto cria uma nova chave no dicionário e inicia o valor da posição
            position_sums[pos] = v

    # cria uma lista com as chaves do dicionário
    positions = list(position_sums.keys())
    # ordena essa lista de forma crescente
    positions.sort()
    # pega item a item na lista
    for pos in positions:
        # pra cada item, apresenta a linha (pos[0]), coluna (pos[1]) e o valor da soma dessa posição no dicionário
        print(pos[0], pos[1], position_sums[pos])
