# instancia uma lista que contém todos os estados da região Norte do Brasil
northern_states = [
    'roraima',
    'acre',
    'amapa',
    'amazonas',
    'para',
    'rondonia',
    'tocantins'
]

# verifica se o Estado que foi digitado no `input()` está contido na lista dos Estados do Norte
if northern_states.__contains__(input()):
    # o Estado digitado faz parte da lista, portanto apresenta "Regiao Norte" na tela
    print('Regiao Norte')
else:
    # o Estado digitado não faz parte da lista, portanto apresenta "Outra regiao" na tela
    print('Outra regiao')
