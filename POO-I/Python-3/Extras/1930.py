plugs = [int(w) for w in input().split()]

total = 1
for plug in plugs:
    total += plug-1

print(total)
