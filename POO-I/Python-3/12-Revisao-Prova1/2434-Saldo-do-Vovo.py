N, S = [int(w) for w in input().split()]

total = S
lowest = S

for i in range(N):
    v = int(input())
    total += v
    if total < lowest:
        lowest = total
print(lowest)
