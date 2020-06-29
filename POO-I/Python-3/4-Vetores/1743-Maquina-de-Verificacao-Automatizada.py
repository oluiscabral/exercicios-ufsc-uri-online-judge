X = [int(x) for x in input().split()]

Y = [int(x) for x in input().split()]

compatible = True
for i in range(len(X)):
    if X[i] == Y[i]:
        compatible = False
        break

if compatible:
    print("Y")
else:
    print("N")
