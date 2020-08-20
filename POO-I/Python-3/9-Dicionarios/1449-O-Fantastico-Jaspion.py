T = int(input())

for i in range(T):
    M, N = [int(w) for w in input().split()]
    translations = {}
    output = ""
    for j in range(M):
        word = input()
        translation = input()
        translations[word] = translation
    for j in range(N):
        output += ' '.join(map(lambda word: translations.get(word,
                                                             word), input().split())) + '\n'
    print(output)
