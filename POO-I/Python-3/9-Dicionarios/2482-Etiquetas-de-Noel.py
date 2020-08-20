translations = {}

for i in range(int(input())):
    language = input()
    translation = input()
    translations[language] = translation

for i in range(int(input())):
    name = input()
    language = input()
    print(name + '\n' + translations[language] + '\n', end='\n')
