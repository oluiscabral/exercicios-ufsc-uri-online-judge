# pega as dimensões da matriz
N, M = [int(w) for w in input().split()]

# variável pra identificar se a matriz corresponde a uma escada
valid = True
# variável pra armazenar o índice do elemento diferente de 0 mais à esquerda da última linha analisada da matriz
last_index = None

# variável que indica que todos os elementos da linha da matriz são iguais a 0
all_zero = False

# itera de 0 a N
for i in range(N):
    # pega a linha da matriz pela entrada do usuário
    line = [int(w) for w in input().split()]

    # verifica se é ainda necessário fazer a validação da matriz
    if valid:
        # a matriz ainda é válida, portanto faz a validação

        # verifica se a última linha da matriz foi toda em 0
        if all_zero:
            # foi, portanto verifica se nessa linha atual tem algum número diferente de 0
            if any(line):
                # a linha atual possui algum número diferente de 0, portanto a matriz não é válida
                valid = False
            # continua o loop, sem ter que passar pelas próximas linhas
            continue

        # nesse caso, a última linha não era composta somente de 0's
        # define que a linha é composta de 0's, até que se prove o contrário
        all_zero = True
        # pega o índice e o número (item) da linha da matriz
        for index, n in enumerate(line):
            # verifica se o número atual é diferente de 0
            if n != 0:
                # o número é diferente de 0, portanto a linha não é composta só por 0's
                all_zero = False
                # para o loop
                break
        # verifica se a linha atual só possui 0's
        if all_zero:
            # a linha atual é toda de 0's, portanto continua o loop
            continue
        # a linha atual não é toda de 0's, então verifica se o índice atual capturado é maior que o último
        if last_index == None or index > last_index:
            # ou o último índice ainda não havia sido iniciado, ou o índice atual obedece às regras do problema
            # atualiza o último índice
            last_index = index
        else:
            # a linha atual não obedece às regras do problema, portanto essa matriz não é válida
            valid = False

# se a matriz for válida (uma escada), apresenta 'S' na tela, caso contrário apresenta 'N'
if valid:
    print('S')
else:
    print('N')
