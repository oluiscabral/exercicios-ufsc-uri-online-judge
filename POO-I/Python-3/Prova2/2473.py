# armazena em listas as apostas e os valores sorteados pela sintaxe de list comprehension
# os inputs são inteiros separados por espaço
bets = [int(w) for w in input().split()]
lottery = [int(w) for w in input().split()]

# instancia uma variável para armazenar a quantidade de combinações entre as listas
matches = 0
# um loop dentro da lista de apostas. Pega as apostas da lista uma a uma
for bet in bets:
    # verifica se o número da aposta também está contido na lista de sorteio
    if lottery.__contains__(bet):
        # a aposta está contida nos números sorteados, portanto soma um no contador de acertos
        matches += 1

# controla o que será imprimido na tela de acordo com a quantidade de acertos na loteria
if matches < 3:
    # o número de acertos é menor que 3, então imprime "azar" na tela
    print('azar')
elif matches == 3:
    # o número de acertos é igual a 3, então imprime "terno" na tela
    print('terno')
elif matches == 4:
    # o número de acertos é igual a 4, então imprime "quadra" na tela
    print('quadra')
elif matches == 5:
    # o número de acertos é igual a 5, então imprime "quina" na tela
    print('quina')
else:
    # o número de acertos é maior que 5, então, por padrão, imprime "sena" na tela
    print('sena')
