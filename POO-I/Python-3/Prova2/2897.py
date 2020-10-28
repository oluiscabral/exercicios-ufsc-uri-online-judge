# define uma função que vai retornar o índice de um elemento dentro de uma lista
def index(list_var, value):
    # cobre o método `index(element)` em um tratamento de erro
    # porque quando um elemento não existe em uma lista, esse método levanta um `ValueError`
    try:
        # se o elemento estiver, retorna seu índice
        return list_var.index(value)
    except ValueError:
        # nesse caso foi levantado um erro, portanto retorna -1 pra indicar que o elemento (value) não está contido na lista
        return -1


# pega um número inteiro a partir da entrada de texto
N = int(input())

# loop que só vai parar de repetir quando N for igual a 0
while N != 0:
    # define a variável que vai guardar o total
    total = 0
    # lista que vai guardar as posições do histórico já utilizadas
    used = []
    # cria uma lista de inteiros a partir do `input()` separado por espaço
    # e pega esses inteiros um a um na variável `p`
    for p in [int(w) for w in input().split()]:
        # pega o índice de p na lista `used`
        i = index(used, p)
        # verifica se o índice de p existe na lista `used`
        if i == -1:
            # não existe, portanto soma o próprio p + o tamanho atual da lista `used` ao total
            total += p + len(used)
        else:
            # existe, portanto soma o índice + 1 ao total
            total += i + 1
        # insere a posição p, pela esquerda, na lista `used`
        used.insert(0, p)
    # apresenta o total
    print(total)
    # pega mais uma vez o valor de N
    N = int(input())
