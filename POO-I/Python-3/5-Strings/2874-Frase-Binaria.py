while True:
    try:

        N = int(input())

        inputedValues = []
        for i in range(N):
            inputedValues.append(int(input(), 2))

        result = ""
        for v in inputedValues:
            result += chr(v)

        print(result)

    except EOFError:
        break
