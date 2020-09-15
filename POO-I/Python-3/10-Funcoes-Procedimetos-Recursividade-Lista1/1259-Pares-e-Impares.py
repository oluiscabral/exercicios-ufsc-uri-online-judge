f = open('o', 'w')
N = int(input())

evens = []
odds = []
for i in range(N):
    value = int(input())
    if value % 2 == 0:
        evens.append(value)
    else:
        odds.append(value)

evens.sort()
odds.sort(reverse=True)

values = evens + odds

output = ""
for value in values:
    output += str(value) + "\n"
output = output[:-1]
f.write(output)
