C = int(input())

for i in range(C):
    testCase = input()
    result = ""
    for c in testCase[::-1]:
        if c.islower():
            result += c

    print(result)
