# entra com o valor de quantos preços serão analisados a seguir
N = int(input())

# inicializa uma variável para armazenar o menor preço
# atribui-se o valor None para não interferir na 1a comparação de preço
lowest = None
# cria-se um loop que se repete N vezes (o i vai de 0 a N-1)
for i in range(N):
    # cria uma lista com os valores da entrada (input()), que é uma str, separados por espaço em branco (split())
    # a maneira utilizada para criar a lista é pela sintaxe de List Comprehensions
    # referência: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
    inp = [w for w in input().split()]
    # pega o primeiro valor do split e armazena e P como float
    P = float(inp[0])
    # pega o primeiro valor do split e armazena e G como int
    G = int(inp[1])

    # calcula um multiplicador para o preço, com base no valor de G
    mult = 1000 / G

    # calcula o preço do item
    price = P * mult

    # `lowest == None` verifica se é a primeira entrada
    # `price < lowest` verifica se o preço atual é menor que o menor armazenado
    if lowest == None or price < lowest:
        # o preço atual é menor que o menor armazenado, então amarzena o atual como menor
        lowest = price

# apresenta na tela uma string formatada
# referências: https://pyformat.info/
print("{:.2f}".format(lowest))
