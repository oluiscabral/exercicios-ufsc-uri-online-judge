# pega o número de questões da prova
K = int(input())

# pega as respostas do Desafortunado por list comprehension
wrong_answers = [char for char in input()]

# pega o número de alunos, além do Desafortunado, da turma
N = int(input())

# instancia uma lista que vai conter uma lista pra cada questão (coluna de resposta)
answers_columns = [[] for w in range(K)]

# loop que vai pegar as respostas dos alunos
for i in range(N):
    # cria uma lista por list comprehension com as alternativas que o aluno i assinalou
    answers = [char for char in input()]
    # loop que vai separar as respostas (diferentes das respostas do Desafortunado) por questões
    for j in range(K):
        # resposta da questão j
        answer = answers[j]
        # verifica se a resposta da questão j desse aluno não é igual à resposta da questão j do Desafortunado
        if answer != wrong_answers[j]:
            # não é igual, então adiciona essa resposta na lista que armazena as respostas da questão j dos alunos
            answers_columns[j].append(answer)

# nota total
total = 0
# percorre as respostas separadas por questões
for answers_column in answers_columns:
    # define que o maior número de respostas iguais é 0
    greater_counter = 0
    # percorre as respostas da questão atual
    for answer in answers_column:
        # contador de quantos alunos tiveram a mesma resposta nessa questão
        repeat_counter = answers_column.count(answer)
        # verifica se o contador de repetição dessa resposta for maior que o maior contador
        if repeat_counter > greater_counter:
            # é maior, portanto atualiza o valor do maior contador
            greater_counter = repeat_counter
    # soma o maior contador de repetição de resposta da questão ao total
    total += greater_counter

# apresenta o total
print(total)
