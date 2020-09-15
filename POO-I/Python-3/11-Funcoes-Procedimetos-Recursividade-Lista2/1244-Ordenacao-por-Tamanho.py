def sort(strings):
    vStrings = strings.copy()
    while True:
        for j in range(1, len(strings)):
            if len(strings[j]) > len(strings[j - 1]):
                aux = strings[j]
                strings[j] = strings[j - 1]
                strings[j-1] = aux
        if vStrings != strings:
            vStrings = strings.copy()
        else:
            break
    return strings


N = int(input())

for i in range(N):
    strings = list()
    strings.extend(input().split())
    strLen = len(strings)
    strings = sort(strings)

    output = ""
    for j in range(strLen):
        output += strings[j] + " "
    output = output[:-1]
    print(output)
