textInput = input()

pdecodeResult = ""

for word in textInput.split():
    for c in word[1::2]:
        pdecodeResult += c
    pdecodeResult += ' '

pdecodeResult = pdecodeResult.rstrip()

print(pdecodeResult)
