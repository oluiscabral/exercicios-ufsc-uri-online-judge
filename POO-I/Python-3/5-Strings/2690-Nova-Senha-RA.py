encodings = [
    ['0', "GQaku"],
    ['1', "ISblv"],
    ['2', "EOYcmw"],
    ['3', "FPZdnx"],
    ['4', "JTeoy"],
    ['5', "DNXfpz"],
    ['6', "AKUgq"],
    ['7', "CMWhr"],
    ['8', "BLVis"],
    ['9', "HRjt"],
]

N = int(input())

for i in range(N):
    encoded = ""
    pw = input()
    i = 0
    for c in pw:
        if i < 12:
            if c != ' ':
                for e in encodings:
                    if e[1].find(c) != -1:
                        encoded += e[0]
                        i += 1
                        break
        else:
            break
    print(encoded)
