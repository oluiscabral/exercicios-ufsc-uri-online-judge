L, N = [int(x) for x in input().split()]

wordsToPlural = []
irregularWords = []
vogals = ['a', 'e', 'i', 'o', 'u']

for i in range(L):
    irregularWords.append([x for x in input().split()])

for i in range(N):
    wordsToPlural.append(input())

for word in wordsToPlural:
    wordIsRegular = False
    for i in range(L):
        if word == irregularWords[i][0]:
            wordIsRegular = True
            print(irregularWords[i][1])
            break
    if not wordIsRegular:
        if word.endswith('y') and vogals.count(word[-2]) == 0:
            word = word[:-1] + 'ies'
        elif word.endswith('o') or word.endswith('s') or word.endswith('ch') or word.endswith('sh') or word.endswith('x'):
            word += 'es'
        else:
            word += 's'
        print(word)
