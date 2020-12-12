def check_result(N, M):
    # função que vai checar se é possível pagar usando apenas duas notas
    # pega do escopo global a lista avaiable_notes
    global avaiable_notes
    # cria uma variável para armazenar o tamanho da lista de notas disponíveis
    L = len(avaiable_notes)

    # define qual a diferença entre os dois valores
    remain = M - N
    # verifica primeiro se vai ser possível achar 2 notas de troco
    if remain < avaiable_notes[1]:
        return False
    # i vai de 0 até L-1
    for i in range(L-1):
        # define uma variável para armazenar o valor da primeira nota
        first_note = avaiable_notes[i]
        # variável que vai armazenar a subtração da diferença com o valor da primeira nota
        test = remain - first_note
        # verifica se com essa nota ainda é possível ter 2 notas de troco
        if test < avaiable_notes[i + 1]:
            return False
        # j vai de i+1 até L
        for j in range(i+1, L):
            # define uma variável para o valor da segunda nota
            second_note = avaiable_notes[j]
            # verifica se a segunda nota é a ideal
            if test - second_note == 0:
                return True
            elif test < second_note:
                # quebra o loop se o teste for menor que a segunda, porque as notas seguintes serão todas menores, portanto não possíveis
                break


# lista que armazena as notas possíveis
avaiable_notes = [2, 5, 10, 20, 50, 100]
# somente por questões demonstrativas da lógica usada, deixa a lista em ordem crescente
# o ordenamento da lista vai importar na função check_result
avaiable_notes.sort()

# loop que se repete até que seja quebrado
while True:
    # pega dois valores da entrada
    N, M = [int(w) for w in input().split()]
    # se os dois valores forem iguais a 0, quebra o loop
    if N == 0 and M == 0:
        break
    # verifica se os valores são possíveis
    if check_result(N, M):
        print("possible")
    else:
        print("impossible")
