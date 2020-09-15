while True:
    try:
        N = int(input()) - 1
        seq = 0
        r = 1
        for i in range(1, N):
            aux = r
            if i % 2 == 0:
                r = r * seq
            else:
                r += seq
            seq = aux
        if N != 0:
            print(r)
        else:
            print(seq)
    except EOFError:
        break
