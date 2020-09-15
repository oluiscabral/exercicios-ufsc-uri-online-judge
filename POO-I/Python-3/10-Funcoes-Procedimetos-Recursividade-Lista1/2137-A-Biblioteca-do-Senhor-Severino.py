def addBook(code):
    global codes
    for j in range(len(codes)):
        if code < codes[j]:
            codes.insert(j, code)
            return True
    codes.append(code)


while True:
    try:
        N = int(input())
        codes = []
        for i in range(N):
            addBook(input())
        for code in codes:
            print(code)
    except EOFError:
        break
