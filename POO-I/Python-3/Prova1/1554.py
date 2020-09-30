# pega um inteiro C que determina a quantidade de casos de teste que vem a seguir
C = int(input())

# loop que vai de 0 até C, com C não incluso
for i in range(C):
    # pega um inteiro N, que define o número de bolas disponíveis, além da branca
    N = int(input())
    # pega por list comprehension a posição da bola branca
    white_x, white_y = [int(w) for w in input().split()]
    # define um dicionário para armazenar os dados da menor distância
    lowest = {}
    # boolean para verificar se o dicionário já foi utilizado
    has_lowest = False
    # loop de 0 até N, com N não incluso
    for j in range(N):
        # pega a posição, por list comprehension, de uma bola qualquer
        x, y = [int(w) for w in input().split()]
        # captura a distância da bola atual até a bola branca
        distance = (white_x - x)**2 + (white_y - y)**2
        # verifica se já existe algum valor para menor número
        # e, se houver, verifica se a distância atual é menor que a distância capturada
        if not has_lowest or distance < lowest['d']:
            # ou ainda não foi definido uma menor distância, ou a distância atual é a menor
            # portanto redefine o boolean de controle
            has_lowest = True
            # armazena (ou substitui) o índice que a menor distância atual foi capturada
            lowest['n'] = j
            # armazena (ou substitui) o valor da menor distância
            lowest['d'] = distance
    # apresenta o número da bola
    print(str(lowest['n']+1))
