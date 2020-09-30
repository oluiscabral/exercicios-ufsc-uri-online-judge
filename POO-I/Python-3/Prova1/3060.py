# entra com o valor total (número inteiro)
V = int(input())
# entra com a quantidade de parcelas
P = int(input())

# calcula o valor inteiro de cada parcela
divided_value = V // P
remainder = V % P

# cria um loop que se repete P vezes
for i in range(P):
    # instancia uma variável para apresentar na tela
    printable_value = divided_value
    # verifica se tem sobra na divisão das parcelas
    if remainder > 0:
        # tem sobra, portanto aumenta o valor que será apresentado em 1
        printable_value += 1
        # diminui o valor da sobra em 1
        remainder -= 1
    # apresenta na tela o valor de cada parcela + (conditional) remainder adder
    print(printable_value)
