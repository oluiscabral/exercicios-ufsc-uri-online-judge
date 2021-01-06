available = [int(w) for w in input().split()]

requests = [int(w) for w in input().split()]

total = sum([b - a for a, b in zip(available, requests) if b > a])

print(total)
