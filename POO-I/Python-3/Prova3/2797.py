def index(lst, value, index):
    # cria uma função para pegar o índice de um item em lista
    # tratamento de erro
    try:
        # retorna o índice caso o item exista
        return lst.index(value, index)
    except ValueError:
        # retorna -1 indicando que o item não existe na lista
        return - 1


def get_index_diff(column, value, init):
    # cria uma função pra pegar a diferença entre 2 índices
    index_1 = index(column, value, init)
    index_2 = index(column, value, index_1+1)
    # define a diferença por padrão igual a 0
    diff = 0
    # verifica se os 2 índices foram encontrados
    if index_1 != -1 and index_2 != -1:
        # todos os índices foram encontrado
        diff = index_2 - index_1
    return diff


# pega os 3 valores do problema
N, M, C = [int(w) for w in input().split()]

# cria uma lista que contêm M listas internas
classrom = [[] for i in range(M)]

# itera N vezes
for i in range(N):
    # cria uma lista com os valores de entrada separados por ' '
    line = [int(w) for w in input().split()]
    # itera M vezes
    for j in range(M):
        # separa as entradas por coluna
        classrom[j].append(line[j])

# inicializa a variável que vai identificar se a organização da sala está correta
valid = True
# inicializa a variável que vai identificar se a última fileira analisada estava ocupada
last_column_occupied = False

# pega coluna por coluna da lista de organização da sala
for column in classrom:
    # verifica se a coluna atual está ocupada
    column_occupied = any(column)

    # verifica se a coluna anterior e a atual está ocupada
    if last_column_occupied and column_occupied:
        # está ocupada, portanto a organização da sala não é válida
        valid = False
        break
    # atualiza a variável de última coluna ocupada
    last_column_occupied = column_occupied

    # se a coluna atual estiver vazia, pula pra próxima
    if not column_occupied:
        continue

    # cria variáveis para verificar se todos os testes 1 ou testes 2 já foram tratados na coluna
    got_all_1 = False
    got_all_2 = False
    for i in range(N - 1):
        # se todos já foram tratados, não faz sentido continuar avaliando
        if got_all_1 and got_all_2:
            break
        # verifica se o teste 1 ainda não foi totalmente tratado
        if not got_all_1:
            # pega a diferença entre o índice do próximo item da coluna (i+1) com o atual (i)
            diff_test_1 = get_index_diff(column, 1, i)
            # atualiza a variável de controle
            got_all_1 = diff_test_1 == 0
        if not got_all_2:
            diff_test_2 = get_index_diff(column, 2, i)
            got_all_2 = diff_test_2 == 0

        # verifica se a diferença entre os índices é menor ou igual ao mínimo esperado
        if (not got_all_1 and diff_test_1 <= C) or (not got_all_2 and diff_test_2 <= C):
            # é menor ou igual, portanto a organização é inválida
            valid = False
            break


# verifica se a sala está com uma organização válida
if valid:
    # está, portanto apresenta 'S' na tela
    print('S')
else:
    # não está, portanto apresenta 'N' na tela
    print('N')
