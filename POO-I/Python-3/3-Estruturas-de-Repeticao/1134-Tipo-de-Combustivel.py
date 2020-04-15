entrada = int(input())

alcool = int(0)
gasolina = int(0)
diesel = int(0)

while entrada != 4:
    if entrada >= 1 and entrada < 4:
        if entrada == 1:
            alcool += 1
        else:
            if entrada == 2:
                gasolina += 1
            else:
                diesel += 1
    entrada = int(input())

print("MUITO OBRIGADO")
print("Alcool: "+ str(alcool))
print("Gasolina: "+ str(gasolina))
print("Diesel: "+ str(diesel))