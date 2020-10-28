# cria um loop que se repete infinitamente
while True:
    # inicia a parte que vai controlar o fim do loop
    try:
        # etapas de o que foi feito na linha 9:
        # 1. pega o que foi digitado no `input()`
        # 2. repõe todos os ' ,' do texto por ','
        # 3. pega o resultado da reposição anterior e repõe todos os ' .' do texto por '.'
        # 4. armazena o resultado de todas as etapas na variável `corrected`, que representa o texto corrigido
        corrected = input().replace(' ,', ',').replace(' .', '.')
        # apresenta na tela o texto já corrigido
        print(corrected)
    # fim da parte que controla o fim do loop
    # EOFError representa o erro que é levantado quando o arquivo atual é fechado durante a execução
    except EOFError:
        # o arquivo foi fechado durante a execução, portanto quebra (para) o loop
        break
