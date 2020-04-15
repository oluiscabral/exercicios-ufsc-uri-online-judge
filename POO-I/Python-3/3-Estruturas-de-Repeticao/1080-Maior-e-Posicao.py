X = []

for i in range(1, 101):
    X.append(int(input()))

maior = max(X)

print(maior)
print(X.index(maior) + 1)