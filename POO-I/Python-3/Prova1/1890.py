# entra com o valor de casos de teste
T = int(input())

# loop que se repete T vezes
for i in range(T):
    # pega o valor de C e D através de uma lista obtida por list compreension no valor do input() separado por espaço (split())
    C, D = [int(w) for w in input().split()]
    # define o total como 0
    total = 0
    # verifica se tanto o C, tanto o D são iguais a 0
    if C != 0 or D != 0:
        # não são iguais a 0, portanto calcula as possibilidades utilizando os valores dados no enunciado
        total = 26 ** C * 10 ** D
    # apresenta o valor do total na tela
    print(total)
