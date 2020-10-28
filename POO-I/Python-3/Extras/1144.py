N = int(input())+1

for i in range(1, N):
    n1, n2 = i, i ** 2
    n3 = n1 * n2
    print(f"{n1} {n2} {n3}")
    print(f"{n1} {n2+1} {n3+1}")
