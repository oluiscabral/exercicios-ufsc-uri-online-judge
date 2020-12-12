def get_surface_range(content, index):
    # função que retorna o começo e o fim da surperfície, partindo do index
    if content[index] != '#':
        return None
    init = index
    end = index + 1
    for c in reversed(content[:index]):
        if c == '#':
            init -= 1
        else:
            break
    if index + 1 < len(content):
        for c in content[index + 1:]:
            if c == '#':
                end += 1
            else:
                break
    return (init, end)


def update_content(content, init, end):
    # função que atualiza com 'o' o range de init, end do conteúdo
    for i in range(init, end):
        content[i] = 'o'


def update_upper_and_bottom_content(upper, bottom):
    # função que atualiza a lista de cima e de baixo, de acordo com o valor dos char's da lista de cima
    global M
    i = 0
    while i < M:
        next_i = i+1
        if upper[i] == 'o':
            surface_range = get_surface_range(bottom, i)
            if surface_range == None:
                bottom[i] = 'o'
            else:
                init, end = surface_range
                if init-1 > -1:
                    upper[init-1] = 'o'
                    bottom[init - 1] = 'o'
                if end < M:
                    upper[end] = 'o'
                    bottom[end] = 'o'
                update_content(upper, init, end)
                next_i = end + 1
        i = next_i


# pega os valores da entrada
N, M = [int(w) for w in input().split()]

# variável pra guardar a matriz
matrix = []
for i in range(N):
    matrix.append([w for w in input()])

# pega linha a linha da matriz (até a penúltima linha)
for i in range(N - 1):
    update_upper_and_bottom_content(matrix[i], matrix[i+1])

# apresenta o resultado
for line in matrix:
    print(''.join(line))
