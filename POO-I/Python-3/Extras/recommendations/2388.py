N = int(input())

total = 0
for i in range(N):
    T, V = [int(w) for w in input().split()]
    total += T * V

print(total)
