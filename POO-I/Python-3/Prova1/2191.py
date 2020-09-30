# entra com o número de quantas partidas serão analisadas a seguir
N = int(input())

# contador para numerar os casos de teste
counter = 1
# loop que para de iterar quando N for igual a 0
while N != 0:
    # define as variáveis para comparar o melhor e o atual período
    # dicionário que armazena o melhor período
    best_streak = {
        'initial': 0,
        'end': 0,
        'score': 0,
    }
    # dicionário que armazena o período atual
    streak = {
        'initial': 0,
        'end': 0,
        'score': 0
    }
    # loop que vai de 0 até N
    for i in range(N):
        # entra com os valores de X e Y, separados por espaço em branco
        X, Y = [int(w) for w in input().split()]
        # atualiza o saldo de gols do período atual
        streak['score'] += X - Y
        # atualiza o fim do período atual
        streak['end'] = i
        # verifica se o período atual tem uma soma de saldo de gols maior que 0
        if streak['score'] >= 0:
            # o período atual tem a soma de saldo de gols maior que 0
            # portanto verifica se o saldo atual é maior que o saldo do melhor período
            # ou, se houve empate nos saldos, verifica se o tamanho do período atual é maior que o do melhor período
            if streak['score'] > best_streak['score'] or (streak['score'] == best_streak['score'] and (streak['end'] - streak['initial'] > best_streak['end'] - best_streak['initial'])):
                # o período atual cumpriu algum dos requisitos
                # então atualiza o melhor período, copiando o (dicionário do) período atual
                # temos que copiar, porque iremos utilizar o streak novamente
                # e, atribuições de objetos são apenas ponteiros
                # i.e.: mudando o streak posteriormente, mudaria o best_streak consequentemente
                best_streak = streak.copy()
        else:
            # o período atual tem soma de saldo menor que 0, portanto reseta o saldo
            # e atualiza o início
            streak['score'] = 0
            # é atribuido +1 no início, porque este índice receberá +1 no próximo loop
            streak['initial'] = i+1

    # neste ponto já temos o melhor período, portanto apresenta na tela
    print('Teste ' + str(counter))
    # verifica se o saldo do melhor período é maior que 0
    if best_streak['score'] > 0:
        # o saldo do melhor período é maior que 0,
        # portanto apresenta o início e o fim do período na tela
        print('{} {}'.format(
            best_streak['initial'] + 1, best_streak['end']+1))
    else:
        # o saldo do melhor periodo é menor ou igual a 0,
        # portanto apresenta 'nenhum' na tela
        print('nenhum')
    # imprime uma linha em branco
    print('')

    # entra novamente com o valor de N
    N = int(input())
    # atualiza o contador
    counter += 1
