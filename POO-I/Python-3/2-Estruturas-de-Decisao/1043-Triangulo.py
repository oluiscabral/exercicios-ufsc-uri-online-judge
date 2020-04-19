A, B, C = [float(x) for x in input().split()]

triangulo = False

if A + B > C and C > ((A - B)**2)**0.5:
    if A + C > B and B > ((A - C)**2)**0.5:
        if B + C > A and A > ((B - C)**2)**0.5:
            triangulo = True

if triangulo:
    print("Perimetro = {0:.1f}".format(A + B + C))
else:
    print("Area = {0:.1f}".format( (A + B) / 2 * C ))