# pega os valores de entrada pedido no enunciado
N, G = [int(w) for w in input().split()]

# define um dicionário pra armazenar o valores das runas que foram digitadas na entrada
runes = {}
# loop que vai de 0 a N-1
for i in range(N):
    # pega os valores da runa
    R, V = [w for w in input().split()]
    # atribui a runa no dicionário
    runes[R] = int(V)

# pega o valor pedido no enunciado
X = int(input())
# define uma variável para armazenar os pontos
points = 0
# pega runa a runa da entrada de texto (separada por um espaço)
for rune in [w for w in input().split()]:
    # atribui os pontos da runa respectiva
    points += runes[rune]

# apresenta a quantidade de pontos
print(str(points))
# verifica se os pontos são menores que o mínimo
if points < G:
    print("My precioooous")
else:
    print("You shall pass!")
