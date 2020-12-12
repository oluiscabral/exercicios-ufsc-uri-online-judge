# loop que se repete até ser quebrado
while True:
    # try-except que vai tratar fins de arquivo
    try:
        # pega a string do número digitado
        N = input()
        # cria um dicionário para armazenar a quantidade de repetição de cada número
        number_uses = {}
        # pega número a número da entrada
        for c in N:
            # verifica se o número já está no dicionário
            if c in number_uses:
                number_uses[c] += 1
            else:
                number_uses[c] = 1
        # define uma variável pra armazenar o número mais repetido
        most_used = None
        # pega chave a chave do dicionário
        for key in number_uses:
            # pega o número de usos do número atual
            uses = number_uses[key]
            # verifica se o mais usado já foi definido ou se o atual é mais usado que o armazenado ou se o número atual é maior que o armazenado
            if most_used is None or uses > most_used[1] or (uses == most_used[1] and key > most_used[0]):
                most_used = (key, uses)
        # apresenta o mais usado
        print(most_used[0])
    except EOFError:
        # quebra o loop caso encontre um EOFError (fim de arquivo)
        break
