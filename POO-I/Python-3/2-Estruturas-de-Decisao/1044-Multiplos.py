A, B = [int(x) for x in input().split()]

maior, menor = 0, 0
multiplos = False

if A > B:
    maior = A
    menor = B
elif B > A:
    maior = B
    menor = A
else:
    multiplos = True

if not multiplos:
    if maior % menor == 0:
        multiplos = True
    
if multiplos:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")