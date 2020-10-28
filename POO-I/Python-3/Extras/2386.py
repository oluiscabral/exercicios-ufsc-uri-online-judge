A = int(input())
N = int(input())

required = 40000000
counter = 0
for i in range(N):
    F = int(input())
    if not (A * F < required):
        counter += 1

print(counter)
