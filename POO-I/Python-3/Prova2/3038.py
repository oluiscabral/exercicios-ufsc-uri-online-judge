# cria um dicionário dos caracteres que serão usados na criptografia, junto aos caracteres que eles representam
# as keys do dicionário são os caracteres utilizados na criptografia
# os values do dicionário são os caracteres criptografados
decrypt_dict = {
    '@': 'a',
    '&': 'e',
    '!': 'i',
    '*': 'o',
    '#': 'u'
}
# pega uma lista contendo as keys do dicionário `decrypt_dict`
decrypt_keys = decrypt_dict.keys()

# cria um loop que se repete infinitamente
while True:
    # inicia a parte que vai controlar o fim do loop
    try:
        # instancia a variável que vai armazenar a mensagem descriptografada
        output = ''
        # percorre caractere a caractere de o que foi digitado no `input()`
        for char in input():
            # verifica se o caractere atual faz parte dos caracteres que são usados na criptografia
            if decrypt_keys.__contains__(char):
                # o caractere atual está criptografado, portanto adiciona ao `output` o caractere que ele representa
                output += decrypt_dict[char]
            else:
                # o caractere atual não está criptografado, então adiciona ele normalmente ao `output`
                output += char
        # apresenta a mensagem descriptografada na tela
        print(output)
    # fim da parte que controla o fim do loop
    # EOFError representa o erro que é levantado quando o arquivo atual é fechado durante a execução
    except EOFError:
        # o arquivo foi fechado durante a execução, portanto quebra (para) o loop
        break
