# pega a quantidade de casos de testes
N = int(input())

# instancia as variáveis que vão armazenar a quantidade de meninos e meninas dos casos de testes
males = 0
females = 0
# loop que se repete N vezes
for i in range(N):
    # Cria uma lista (utilizando a sintaxe de list comprehension) com os valores do `input()` separados por espaço.
    # Depois de criada a lista, pega o último elemento dela.
    # O último elemento da lista corresponde ao char que identifica se a criança é um menino ('M') ou uma menina ('F').
    # Atribui o char de identificação a variável `gender`
    gender = [w for w in input().split()][1]
    # verifica se o char corresponde a um menino
    if gender == 'M':
        # é um menino, portanto adiciona 1 ao contador de meninos
        males += 1
    else:
        # o char não é M, portanto, por padrão, a entrada do caso de teste atual é uma menina. Adiciona um ao contador de meninas
        females += 1

# apresenta na tela a saída especificada pelo problema
print(str(males) + " carrinhos")
print(str(females) + " bonecas")
