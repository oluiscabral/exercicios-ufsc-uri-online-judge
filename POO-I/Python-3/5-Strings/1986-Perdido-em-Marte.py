result = ""

n = int(input())
hexaDecimalChars = [x for x in input().split()]

for hexaDecimalChar in hexaDecimalChars:
    result += chr(int(hexaDecimalChar, 16))

print(result)
