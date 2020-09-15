N = int(input())

outputs = []
for i in range(N):
    outputs.append("")
    items = []
    for item in input().split():
        if item not in items:
            items.append(item)
    items.sort()
    for item in items:
        outputs[i] += item + " "
    outputs[i] = outputs[i][:-1]

for output in outputs:
    print(output)
