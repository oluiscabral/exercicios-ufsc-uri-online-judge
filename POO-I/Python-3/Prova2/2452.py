# define uma função pra marcar pontos na fita
def mark_tape(tape, marks_p):
    # percorre os inteiros da lista `marks_p`
    for p in marks_p:
        # marca o índice da posição na fita
        tape[p] = True
    # retorna a fita depois das marcações
    return tape

# define uma função que retorna os próximos pontos a serem marcados na fita


def get_new_marks(tape, i):
    # pega a variável global que define quantas posições tem a fita
    global F
    # cria uma lista para retornar as novas (próximas) marcações
    new_marks_p = []
    # lista que guarda as possibilidades de marcação na lista (esquerda e direita)
    possibilities = [i - 1, i + 1]
    # percorre as posições possíveis
    for p in possibilities:
        # verifica se a posição é maior ou igual a 0, se a posição é menor que o tamanho total da fita e se a posição não está marcada
        if p > -1 and p < F and not tape[p]:
            # a posição cumpre os requisitos, portanto adiciona ela como nova marcação
            new_marks_p.append(p)
    # retorna as novas marcações
    return new_marks_p


# pega, por list comprehension, inteiros da entrada (`input()`) separados por espaço
F, R = [int(w) for w in input().split()]

# cria a lista que vai guardar as marcações na fita
tape = [False for w in range(F)]

# cria uma lista que vai marcar os últimos pontos que foram marcados na fita
last_marks_p = []

# percorre a lista de posições que serão marcadas inicialmente
# a lista foi criada por list comprehension e converte cada valor do input() separado por espaço
for position in [int(w) - 1 for w in input().split()]:
    # marca os pontos da posição na fita
    tape[position] = True
    # adiciona os pontos iniciais na lista de últimas marcações
    last_marks_p.append(position)

# inicia a variável que vai armazenar quantas etapas foram necessárias para marcar toda a fita
counter = 0
# loop que para com um controlador
while True:
    # cria a lista que vai armazenar novos pontos
    new_marks_p = []
    # variável booleana que vai verificar se a lista já foi totalmente preenchida
    had_new_marks = False
    # percorre as posições das últimas marcações
    for p in last_marks_p:
        # armazena em uma variável temporária as novas marcações
        temp_new_marks_p = get_new_marks(tape, p)
        # verifica se foi pego novos pontos a serem marcados
        if len(temp_new_marks_p) > 0:
            # achou novos pontos, portanto adiciona eles a lista de novos pontos e atualiza a variável booleana de controle
            new_marks_p.extend(temp_new_marks_p)
            had_new_marks = True
    # verifica se foi achado novos pontos
    if had_new_marks:
        # foi achado novos pontos, portanto atualiza a fita com eles
        tape = mark_tape(tape, new_marks_p)
        # atualiza os últimos pontos que foram pegos
        last_marks_p = new_marks_p
        # atualiza o contador
        counter += 1
    else:
        # não foi achado pontos novos, a lista já foi totalmente preenchida, portanto quebra (para) o loop
        break
# imprime na tela o contador
print(counter)
