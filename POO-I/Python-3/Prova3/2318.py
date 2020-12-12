def resolve(lines, diagonal_handler=None):
    # função recursiva que retorna a matriz resolvida ou None se a matriz não tiver solução
    # pega as coluna por coluna da matriz
    columns = [[] for i in range(3)]
    for line in lines:
        for i in range(3):
            columns[i].append(line[i])

    # pega as duas diagonais da matriz
    diagonals = [[] for i in range(2)]
    for i in range(3):
        diagonals[0].append(lines[i][i])
        diagonals[1].append(lines[i][2-i])

    # se existir alguma linha, coluna ou diagonal completa, pega a soma delas
    base = get_base([lines, columns, diagonals])
    if base != None:
        # existe alguma soma, portanto preenche as listas de linhas e colunas
        lines = get_filled_list(lines, base)
        columns = get_filled_list(columns, base)

        # só por razões de retorno, instancia a variável que vai armazenar a matriz
        matrix = lines
        for i in range(3):
            for j in range(3):
                # verifica se o item da linha é igual a 0
                if not matrix[i][j]:
                    # é igual a 0, então pega o item correspondende na lista de colunas
                    matrix[i][j] = columns[j][i]

        # verifica se a função atual foi chamada recursivamente por método bruteforce de resolução
        if diagonal_handler != None:
            # essa função foi chamada recursivamente, portanto vamos ver se o número chutado resolve a matriz
            diagonal = []
            if diagonal_handler == True:
                # a diagonal vazia corresponde a diagonal que vai do canto superior direito até o canto inferior esquerdo
                for i in range(3):
                    diagonal.append(matrix[i][2 - i])
                # verifica se a soma é igual a base
                if sum(diagonal) == base:
                    # a matriz é válida, portanto retorna ela
                    return matrix
            else:
                # a diagonal corresponde a diagonal do canto superior esquerdo até o canto inferior direito
                for i in range(3):
                    diagonal.append(matrix[i][i])
                if sum(diagonal) == base:
                    return matrix
            # o número bruteforce atual não é resolução
            return None
    else:
        # nesse caso, alguma diagonal está totalmente vazia
        # portanto vamos checar se essa matriz é formada por números iguais
        valid = True
        # variável que vai armazenar o último número verificado
        last_n = None
        for line in lines:
            for n in line:
                if n != 0:
                    # se o número atual é diferente de 0 e é diferente do último número, essa matriz não é formada por números iguais
                    if last_n != None and n != last_n:
                        valid = False
                        break
                    last_n = n
            if not valid:
                break
        # verifica se a matriz é formada por números iguais
        if valid:
            # é sim formada por um único número, portanto a resolução da matriz é só preencher as lacunas com o mesmo número
            for i in range(3):
                for j in range(3):
                    if lines[i][j] == 0:
                        lines[i][j] = last_n
            matrix = lines
        else:
            # a matriz é formada por números diferentes, portanto checa qual das diagonais está totalmente vazia
            if lines[0].index(0) == 2:
                # a diagonal vazia é a do canto superior direito até o canto inferior esquerdo
                for n in range(1, 20001):
                    # faz check bruteforce do 1 até o 2000
                    lines[0][2] = n
                    matrix = resolve(copy(lines), True)
                    if matrix != None:
                        break
            else:
                # a diagonal vazia é a do canto superior esquerdo até o canto inferior direito
                for n in range(1, 20001):
                    # faz check bruteforce
                    lines[0][0] = n
                    matrix = resolve(copy(lines), False)
                    if matrix != None:
                        break
    # retorna a matriz que foi encontrada
    return matrix


def copy(grid):
    # função pra copiar uma lista de listas
    vGrid = []
    for line in grid:
        vGrid.append(line.copy())
    return vGrid


def get_base(list_of_lists):
    # função de que pega a soma de alguma lista de listas que tem alguma lista interna completa (sem 0's)
    for lst in list_of_lists:
        base = check_all_to_base(lst)
        if base != None:
            return base
    return None


def check_all_to_base(lst):
    # função para retornar a soma de uma linha da lista se a linha estiver completa
    for line in lst:
        if all(line):
            return sum(line)
    return None


def get_filled_list(lst, base):
    # função que preenche uma lista (que contém um e apenas um 0)
    for line in lst:
        if line.count(0) == 1:
            line[line.index(0)] = base - sum(line)
    return lst


# tenta resolver a matriz 3x3 dada pela entrada
matrix = resolve([[int(w) for w in input().split()] for i in range(3)])

# verifica se foi possível resolver a matriz
if matrix != None:
    # foi possível, portanto apresenta a matriz na tela
    for i in range(3):
        print(matrix[i][0], matrix[i][1], matrix[i][2])
