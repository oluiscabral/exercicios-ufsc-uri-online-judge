# cria uma lista pela sintaxe de list comprehension dos valores do `input()` separados por espaço
# armazena os elementos da lista nas variáveis N e K
N, K = [int(w) for w in input().split()]

# cria uma lista pela sintaxe de list comprehesion dos valores do `input()` separados por espaço
arrivals = [int(w) for w in input().split()]

# instancia uma variável para contar quantos alunos chegaram antes do horário ou na hora
on_time = 0

# loop pelos horários de chegada dos alunos
for arrival in arrivals:
    # verifica se o horário de chegada é atrasado
    if arrival < 1:
        # o aluno em questão chegou dentro do horário, portanto soma 1 ao contador de alunos no horário
        on_time += 1

# verifica se o mínimo de alunos no horário foi atingido
if on_time >= K:
    # tem o mínimo de alunos no horário, portanto apresenta "YES" na tela
    print('YES')
else:
    # não tem o mínimo de alunos no horário, portanto apresenta "NO" na tela
    print('NO')
