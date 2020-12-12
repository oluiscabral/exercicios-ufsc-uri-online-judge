# cria um dicionário para armazenar o padrão
pattern = {}
# a letra 'a' é data pelo número 97 como parâmetro no método builtin chr()
base = 97

# pega tanto o índice, tanto o valor do item no dado índice da entrada
for i, char in enumerate(input()):
    # o char atual é a letra que ocupa a posição i do alfabeto (minúsculo)
    pattern[char] = chr(base+i)

# inicializa uma variável para armazenar o texto de saída
output = ''
# pega char a char do que foi inserido na entrada
for char in input():
    # a saída será dada pela letra que representa a letra digitada segundo o padrão criado
    output += pattern[char]

# apresenta o resultado
print(output)
