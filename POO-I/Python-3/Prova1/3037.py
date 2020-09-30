# entra com o número de casos de testes serão feitos
N = int(input())

# loop que se repete N vezes
for i in range(N):
    # inicializa as variáveis que armazenam a quantidade de pontos de João e Maria (individualmente)
    joao_points = 0
    maria_points = 0

    # loop que se repete 3 vezes
    # este loop pega os valores referentes aos arremessos de João
    for j in range(3):
        # armazena em x e em d, os itens da lista gerada pela entrada (str) separada por espaço (split()) e converte os itens em int
        # x = int(lista[0]), d = int(lista[1])
        x, d = [int(w) for w in input().split()]
        # soma os pontos que João já tem com os pontos da entrada atual
        # joao_points = joao_points + x*d
        joao_points += x * d

    # loop que se repete 3 vezes
    # este loop pega os valores referentes aos arremessos de Maria
    for j in range(3):
        # armazena em x e em d, os itens da lista gerada pela entrada (str) separada por espaço (split()) e converte os itens em int
        # x = int(lista[0]), d = int(lista[1])
        x, d = [int(w) for w in input().split()]
        # soma os pontos que Maria já tem com os pontos da entrada atual
        # maria_points = maria_points + x*d
        maria_points += x * d
    # verifica se João fez mais pontos que Maria
    if joao_points > maria_points:
        # João fez mais pontos que Maria, então apresenta "JOAO" na tela
        print("JOAO")
    else:
        # Maria fez mais pontos que João, então apresenta "MARIA" na tela
        print("MARIA")

# nota-se que não existe caso para empate
# portanto, na lógica atual, se João pontuou o mesmo que Maria, Maria é a vencedora
