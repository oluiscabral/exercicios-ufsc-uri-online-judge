# loop que só para de iterar com um `break`
while True:
    # início do tratamento de exceções
    try:
        # pega as dimensões da matriz
        M, N = [int(w) for w in input().split()]
        # inicializa a variável para armazenar a quantidade de sacas
        bags = 0
        # inicializa a variável para armazenar o total de litros
        liters = 0
        # loop que se repete M vezes
        for i in range(M):
            # o total de litros é dado pela soma dos valores da entrada separados por espaço
            liters += sum([int(w) for w in input().split()])
            # verifica se há 60 litros ou mais na linha
            if liters > 59:
                # há sim, portanto verifica quantas vezes 60 cabe no total de litros da linha
                m = liters // 60
                # atualiza o total de litros e o total de sacas
                liters -= m * 60
                bags += m
        # apresenta o resultado conforme o exemplo indicado pelo problema
        print(str(bags) + " saca(s) e " + str(liters) + " litro(s)")
    # trata as exceções do tipo End Of File (EOF), que são as de fim de execução
    except EOFError:
        # o arquivo foi encerrado, portanto quebra o loop
        break
