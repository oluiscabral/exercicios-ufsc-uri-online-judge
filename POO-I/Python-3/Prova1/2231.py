# pega os números N e M por meio da sintaxe de list comprehension
N, M = [int(w) for w in input().split()]

# define o contador do loop (que vai mostrar a ordem dos testes)
counter = 1
# um loop que vai iterar até que tanto o N, tanto o M sejam iguais a 0
while N != 0 or M != 0:
    # define uma lista para armazenar as temperaturas do caso de teste
    temperatures = []
    # iteração para capturar as temperaturas digitadas
    for i in range(N):
        # coloca a entrada (input()) transformada em int
        temperatures.append(int(input()))

    # define o total da soma do primeiro grupo de temperatura
    total = sum(temperatures[0:M])
    # declara as variáveis que vão armazenar a menor e maior soma
    lowest = total
    highest = total

    # cria um loop que define o i de 0 até N-M+1
    for i in range(1, N - M + 1):
        c = i - 1
        total += temperatures[c+M] - temperatures[c]
        # verifica se o total atual é menor ou maior que o menor e maior total
        if total < lowest:
            # é menor, então redefine o menor capturado
            lowest = total
        if total > highest:
            # é maior, então redefine o maior capturado
            highest = total

    # apresenta, conforme a formatação solicitada, a menor e maior média de temperatura
    print('Teste ' + str(counter))
    print('{} {}'.format(int(lowest/M), int(highest/M)))
    print('')

    # pega novamente os valores de N e M
    N, M = [int(w) for w in input().split()]
    # atualiza o contador de testes
    counter += 1
