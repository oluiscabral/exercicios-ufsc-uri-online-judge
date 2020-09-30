# entra com a idade da Dona Mônica
M = int(input())

# entra com a idade de 2 filhos, um em cada linha
A = int(input())
B = int(input())

# calcula a idade do 3o filho
# idade do 3o filho é igual a idade da Dona Mônica menos a idade dos dois outros filhos somadas
C = M - A - B

# pega o maior número de uma lista (o valor da idade do mais velho) com o método builtin max
oldest = max([A, B, C])

# apresenta o valor da idade do filho mais velho
print(oldest)
