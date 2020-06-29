N = int(input())

X = [int(x) for x in input().split()]

minValue = min(X)
print("Menor valor: " + str(minValue))
print("Posicao: " + str(X.index(minValue)))
