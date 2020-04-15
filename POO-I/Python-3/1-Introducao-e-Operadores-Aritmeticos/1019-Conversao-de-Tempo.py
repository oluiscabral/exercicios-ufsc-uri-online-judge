N = int(input())

segundos = N % 60

minutos = N // 60

horas = minutos // 60

minutos = minutos - horas * 60

print(str(horas) + ":" + str(minutos) + ":" + str(segundos))