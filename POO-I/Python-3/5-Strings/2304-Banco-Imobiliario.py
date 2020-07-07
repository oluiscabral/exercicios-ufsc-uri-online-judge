def operation(player, value):
    global DMoney, EMoney, FMoney
    if player == 'D':
        DMoney += value
    elif player == 'E':
        EMoney += value
    else:
        FMoney += value


I, N = [int(x) for x in input().split()]

DMoney = I
EMoney = I
FMoney = I

for i in range(N):
    operationStatement = [x for x in input().split()]
    operationValue = int(operationStatement[-1])

    if operationStatement[0] == 'C':
        operation(operationStatement[1], operationValue*-1)
    elif operationStatement[0] == 'V':
        operation(operationStatement[1], operationValue)
    else:
        operation(operationStatement[1], operationValue)
        operation(operationStatement[2], operationValue*-1)

print(str(DMoney)+" "+str(EMoney)+" "+str(FMoney))
