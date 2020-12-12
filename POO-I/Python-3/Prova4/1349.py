# por razões de tempo de execução, as funções tratam as matrizes sem antes copiá-las
# não copiar a matriz == mudar a matriz de entrada e retornar a mesma

def get_reversed_matrix(matrix):
    # define uma função que inverte a matriz do parâmetro
    reversed_matrix = []
    for line in matrix:
        reversed_matrix.append([])
        line.reverse()
        for v in line:
            reversed_matrix[-1].append(v)
    return reversed_matrix


def get_copied_matrix(matrix):
    # função que copia a matriz do parâmetro
    copied_matrix = []
    for line in matrix:
        copied_matrix.append([])
        for value in line:
            copied_matrix[-1].append(value)
    return copied_matrix


def get_left_rotated_matrix(matrix):
    # função que rotaciona a matriz do parâmetro
    global L
    left_rotated_matrix = [[] for i in range(L)]
    for line in matrix:
        line.reverse()
        for i in range(L):
            left_rotated_matrix[i].append(line[i])
    return left_rotated_matrix


def get_matrix_from_input():
    # função que pega uma matriz de tamanho L de linhas e colunas
    global L
    matrix = []
    for i in range(L):
        matrix.append([int(w) for w in input().split()])
    return matrix


def get_precision(first_matrix, second_matrix) -> float:
    # compara a primeira matriz, normal e invertida, com a segunda
    normal_precision = compare_matrices(first_matrix, second_matrix)
    reversed_precision = compare_matrices(get_reversed_matrix(
        get_copied_matrix(first_matrix)), second_matrix)
    return max(normal_precision, reversed_precision)


def compare_matrices(first_matrix, second_matrix) -> float:
    # compara as duas matrizes e retorna a precisão
    global L
    base_compare = L ** 2
    in_range_counter = 0
    for i in range(L):
        for j in range(L):
            if abs(first_matrix[i][j] - second_matrix[i][j]) < 101:
                in_range_counter += 1
    if in_range_counter == base_compare:
        return 100.00
    else:
        return round((in_range_counter*100)/base_compare, 2)


def full_compare_matrices(first_matrix, second_matrix) -> float:
    # compara as matrizes por completo
    greatest_precision = get_precision(first_matrix, second_matrix)
    if greatest_precision == 100.00:
        return 100.00
    temp_matrix = first_matrix
    for i in range(3):
        temp_matrix = get_left_rotated_matrix(temp_matrix)
        precision = get_precision(temp_matrix, second_matrix)
        if precision == 100.00:
            return 100.00
        if precision > greatest_precision:
            greatest_precision = precision
    return greatest_precision


while True:
    # loop principal do problema
    L = int(input())
    if L == 0:
        break
    first_matrix = get_matrix_from_input()
    second_matrix = get_matrix_from_input()
    precision = full_compare_matrices(first_matrix, second_matrix)
    print('{:.2f}'.format(precision))
