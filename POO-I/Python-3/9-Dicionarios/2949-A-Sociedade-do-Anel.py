members = {
    'X': [0, "Hobbit(s)"],
    'H': [0, "Humano(s)"],
    'E': [0, "Elfo(s)"],
    'A': [0, "Anao(s)"],
    'M': [0, "Mago(s)"]
}
N = int(input())
if N > 0:
    for i in range(N):
        members[(input().split())[1]][0] += 1
    output = ""
    for key in members.keys():
        output += str(members[key][0]) + ' ' + members[key][1] + '\n'
    print(output[:-1])
