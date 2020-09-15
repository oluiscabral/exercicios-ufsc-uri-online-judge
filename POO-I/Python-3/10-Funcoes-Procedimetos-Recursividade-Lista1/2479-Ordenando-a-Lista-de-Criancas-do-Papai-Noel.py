names = []
wellBehaved = 0
misbehaved = 0


def addChild(inp):
    global names, wellBehaved, misbehaved
    if inp[0] == '+':
        wellBehaved += 1
    else:
        misbehaved += 1
    for j in range(len(names)):
        if inp[1] < names[j]:
            names.insert(j, inp[1])
            return True
    names.append(inp[1])


for i in range(int(input())):
    addChild(input().split())

output = ""
for name in names:
    output += name + '\n'

output += "Se comportaram: " + \
    str(wellBehaved) + " | Nao se comportaram: " + str(misbehaved)

print(output)
