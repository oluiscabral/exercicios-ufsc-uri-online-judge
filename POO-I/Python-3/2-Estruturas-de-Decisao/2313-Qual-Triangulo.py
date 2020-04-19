A, B, C = [float(x) for x in input().split()]

triangulo = False

if A + B > C and C > ((A - B)**2)**0.5:
    if A + C > B and B > ((A - C)**2)**0.5:
        if B + C > A and A > ((B - C)**2)**0.5:
            triangulo = True

if triangulo:
    if A == B and A == C:
        #triangulo equilatero
        print("Valido-Equilatero")
    elif A == B or A == C or B == C:
        #triangulo isoceles
        print("Valido-Isoceles")
    else:
        #escaleno
        print("Valido-Escaleno")

    if A**2 + B**2 == C**2 or A**2 + C**2 == B**2 or B**2 + C**2 == A**2:
        print("Retangulo: S")
    else:
        print("Retangulo: N")
else:
    print("Invalido")