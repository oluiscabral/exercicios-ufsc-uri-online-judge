# cria uma lista dos valores do `input()` separados por espaço pela sintaxe de list comprehension
# armazena os elementos da lista nas variáveis N, I, F
N, I, F = [int(w) for w in input().split()]
# cria uma lista dos valores do `input()` separados por espaço pela sintaxe de list comprehension
# armazena a lista na variável `vector`
vector = [int(w) for w in input().split()]

# instancia uma variável para contar quantos pares de números somados estão no intevalo `I <= soma <= F`
valid_counter = 0
# loop que vai pegar do primeiro até o penúltimo item da lista vector
for i in range(N - 1):
    # armazena o valor do elemento da posição i da lista vector na variável n1
    n1 = vector[i]
    # loop que vai pegar do elemento i+1 até o último elemento da lista
    for j in range(i + 1, N):
        # armazena a soma do elemento i com o elemento j
        s = n1 + vector[j]
        # verifica se a soma for maior ou igual ao valor mínimo e menor igual ao valor máximo
        if s >= I and s <= F:
            # a soma está no intervalo válido, portanto soma um ao contador
            valid_counter += 1

# apresenta na tela a quantidade de pares somados que estão no intervalo válidos
print(valid_counter)
