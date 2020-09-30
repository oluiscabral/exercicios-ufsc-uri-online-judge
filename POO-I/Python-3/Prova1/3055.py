# pega o valor da nota da 1a prova e o valor da média entre as duas provas (A + B) / 2
A = int(input())
M = int(input())

# calcula o valor da 2a prova utilizando a média entre as provas e o valor da prova A
B = 2 * M - A

# apresenta na tela o valor da prova B
print(B)
