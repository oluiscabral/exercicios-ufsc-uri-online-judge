def get_diagonal_y(x):
    # função que calcula o y da função linear que a diagonal do retângulo do problema descreve
    global k
    return x*k


# pega as informações do problema
n, m, s = [int(w) for w in input().split()]
# calcula a constante da função linear da diagonal do retângulo
k = m/n

# variáveis para armazenar as habilidades somadas de cada exército
team_1_score = 0
team_2_score = 0
# itera s vezes
for i in range(s):
    # pega as coordenadas e habilidade de uma tropa do exército
    x, y, h = [int(w) for w in input().split()]

    # verifica se a coordenada y da tropa é superior ou inferior à diagonal do retângulo
    if y > get_diagonal_y(x):
        # é maior, portanto essa tropa é do 1o time
        team_1_score += h
    else:
        # é menor ou igual, portanto essa tropa é do 2o time
        team_2_score += h

# apresenta o resultado, conforme o exemplo solicitado pelo problema
print(team_1_score, team_2_score)
