def get_match_offsets(text: str, search: str):
    # define uma função para retornar as posições da palavra pesquisada
    # define uma lista de retorno
    ret = []
    # pega o tamanho do texto
    text_len = len(text)
    # pega o tamanho da palavra a ser pesquisada
    search_len = len(search)
    # verifica se o texto contém apenas uma palavra e se essa palavra é a que procuramos
    if text_len == search_len and text == search:
        # retorna uma lista com apenas a posição 0
        return [0]
    # pega a palavra a ser pesquisada no meio do texto
    search_mid = " " + search + " "
    # pega o tamanho da palavra a ser pesquisada no meio do texto
    search_mid_len = search_len + 2
    # define uma variável pra armazenar a posição do final da palavra encontrada
    last_end = 0
    # verifica se o texto começa com a palavra a ser encontrada
    if text.startswith(search + " "):
        last_end = search_len
        ret.append(0)
    # loop que só para se for quebrado
    while True:
        # pega a posição da palavra a ser encontrada partindo da posição `last_end`
        offset = text.find(search_mid, last_end)
        # verifica se foi encontrada alguma palavra
        if offset == -1:
            break
        # adiciona à lista de retorno a posição capturada + 1 (em razão do espaço em branco)
        ret.append(offset + 1)
        # atualiza a variável de final de palavra
        last_end = offset + search_mid_len
    # verifica se o texto termina com a palavra a ser encontrada
    if text.endswith(" " + search):
        ret.append(text_len - search_len)
    # retorna a lista de retorno
    return ret


# pega o valor da quantidade de casos de testes
q = int(input())

# itera de 0 a q-1
for i in range(q):
    # pega o texto de teste
    text = input()
    # pega a palavra a ser procurada
    search = input()
    # pega o retorno da função get_match_offsets
    match_offsets = get_match_offsets(text, search)
    # verifica se a lista não está vazia
    if len(match_offsets) > 0:
        # apresenta na tela, posição a posição (map) da lista match_offsets convertidas para string e com um espaço em branco entre elas `' '.join(`
        print(' '.join(map(str, match_offsets)))
    else:
        print("-1")
