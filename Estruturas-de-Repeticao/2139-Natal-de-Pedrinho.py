while True:
    try:
        entrada = [int(x) for x in input().split()] 

        mes = entrada[0]
        dia = entrada[1]

        dia_mes = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        diferenca = 0

        for i in range(mes, 12):
            diferenca += dia_mes[i-1]
        
        diferenca += 25 - dia

        if diferenca == 0:
            print("E natal!")
        elif diferenca == 1:
            print("E vespera de natal!")
        elif diferenca < 0:
            print("Ja passou!")
        else:
            print("Faltam "+ str(diferenca) + " dias para o natal!")
    except EOFError:
        break