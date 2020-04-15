N = [float(x) for x in input().split(".")]

dinheiro = int(N[0])
moeda = int(N[1])

nota_100 = dinheiro // 100
dinheiro -= nota_100 * 100

nota_50 = dinheiro // 50
dinheiro -= nota_50 * 50

nota_20 = dinheiro // 20
dinheiro -= nota_20 * 20

nota_10 = dinheiro // 10
dinheiro -= nota_10 * 10

nota_5 = dinheiro // 5
dinheiro -= nota_5 * 5

nota_2 = dinheiro // 2
dinheiro -= nota_2 * 2

moeda_1 = dinheiro

moeda_05 = moeda // 50
moeda -= moeda_05 * 50

moeda_025 = moeda // 25
moeda -= moeda_025 * 25

moeda_01 = moeda // 10
moeda -= moeda_01 * 10

moeda_005 = moeda // 5
moeda -= moeda_005 * 5

moeda_001 = moeda

print("NOTAS:")
print(str(nota_100) + " nota(s) de R$ 100.00")
print(str(nota_50) + " nota(s) de R$ 50.00")
print(str(nota_20) + " nota(s) de R$ 20.00")
print(str(nota_10) + " nota(s) de R$ 10.00")
print(str(nota_5) + " nota(s) de R$ 5.00")
print(str(nota_2) + " nota(s) de R$ 2.00")
print("MOEDAS:")
print(str(moeda_1) + " moeda(s) de R$ 1.00")
print(str(moeda_05) + " moeda(s) de R$ 0.50")
print(str(moeda_025) + " moeda(s) de R$ 0.25")
print(str(moeda_01) + " moeda(s) de R$ 0.10")
print(str(moeda_005) + " moeda(s) de R$ 0.05")
print(str(moeda_001) + " moeda(s) de R$ 0.01")