M, N = [int(w) for w in input().split()]

roles = {}

for i in range(M):
    name, wage = input().split()
    roles[name] = int(wage)

for i in range(N):
    text = ""
    total = 0
    line = input()
    while line != '.':
        text += line + " "
        line = input()
    total += sum(map(lambda word: roles.get(word, 0), text.split()))
    print(total)
