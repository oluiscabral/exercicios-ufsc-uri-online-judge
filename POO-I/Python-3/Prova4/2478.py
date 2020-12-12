def check_desires(name, gift):
    # função que checa no dict de desejos se o nome está lista e algum presente da lista de presentes está no desejo da pessoa de respectivo nome
    global desires
    if name in desires and gift in desires[name]:
        return True
    else:
        return False


# define uma mensagem de sucesso
success_message = "Uhul! Seu amigo secreto vai adorar o/"
# define a mensagem de não encontrado
fail_message = "Tente Novamente!"

# define a lista de desejos
desires = {}
# pega a quantidade de nomes armazenados
X = int(input())
# pega os desejos das pessoas digitadas na entrada
for i in range(X):
    inp = input().split()
    desires[inp[0]] = inp[1:]

# loop principal
while True:
    try:
        # pega a entrada
        inp = input().split()
        # usa a função de check de desejos pra verificar o nome (inp[0]) e o presente (inp[1])
        if check_desires(inp[0], inp[1]):
            print(success_message)
        else:
            print(fail_message)
    except EOFError:
        break
