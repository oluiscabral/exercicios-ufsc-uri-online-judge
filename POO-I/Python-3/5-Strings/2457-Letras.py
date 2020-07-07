inputChar = input()

words = input().split()
wordsNumber = len(words)

charUses = 0

for i in range(wordsNumber):
    for c in words[i]:
        if c == inputChar:
            charUses += 1
            break

charUsePercentage = (charUses / wordsNumber) * 100

print(round(charUsePercentage, 1))
