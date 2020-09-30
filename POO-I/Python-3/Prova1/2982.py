# entra com o valor de entradas a seguir
N = int(input())

# inicializa as variáveis que vão conter os valores de verba e despesas, respectivamente, da universidade
funds = 0
expenses = 0
# loop que se repete N vezes
for i in range(N):
    # cria uma lista com os valores do input() separados por espaço (split())
    # referência para a sintaxe de list comprehension usada: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
    inp = [w for w in input().split()]
    # define uma variável para o primeiro item da lista gerada pelo input().split() (um caractere)
    T = inp[0]
    # converte em int o valor do segundo intem da lista gerada
    C = int(inp[1])
    # verifica se o caractere é de gasto da universidade
    if T == 'G':
        # o caractere indica gasto, portanto se deve adicionar C ao gasto total da universidade
        expenses += C
    else:
        # o caractere indica verba, portanto se deve adicionar C à verba total da universidade
        funds += C

# verifica se a verba é superior ao gasto total da universidade
if funds >= expenses:
    # a verba é superior, portanto imprime uma mensagem na tela indicando o fim da greve
    print('A greve vai parar.')
else:
    # a verba é inferior, portanto imprime uma mensagem na tela indicando que a greve continuará
    print('NAO VAI TER CORTE, VAI TER LUTA!')
