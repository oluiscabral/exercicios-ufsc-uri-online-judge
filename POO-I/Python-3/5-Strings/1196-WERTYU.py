base = "`1234567890-=QWERTYUIOP[]\ASDFGHJKL;'ZXCVBNM,./"
while True:
    try:
        I = input()
        result = ""
        for c in I:
            if c != ' ':
                result += base[base.find(c) - 1]
            else:
                result += ' '
        print(result)
    except EOFError:
        break
