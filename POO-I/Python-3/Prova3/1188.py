# pega o char de entrada
O = input()

# cria uma matriz, que é uma lista com 12 listas internas
matrix = [[] for i in range(12)]

# itera de 0 a 11
for i in range(12):
    # itera de 0 a 11 pra cada número de 0 a 11
    for j in range(12):
        # insere na lista interna `i` uma entrada float
        matrix[i].append(float(input()))

# define que o range de início vai de 5 a 6
init = 5
end = 7

# inicializa as variáveis para guardar a soma total e quantidade de células
total = 0
cells_counter = 0

# itera de 7 a 11
for i in range(7, 12):
    # soma o total com a soma dos valores da lista `i`, partindo do item `init` até o `end-1`
    total += sum(matrix[i][init:end])
    # soma o total de células utilizadas
    cells_counter += end - init
    # atualiza o início e o fim da captura de células
    init -= 1
    end += 1

# verifica se o char que foi digitado indica soma ou média
if O == 'S':
    # o char é 'S', portanto o resultado é a própria soma
    result = total
else:
    # o char não é 'S', portanto o resultado é a média das células capturadas
    result = total / cells_counter

# apresenta o resultado na tela
print(result)
