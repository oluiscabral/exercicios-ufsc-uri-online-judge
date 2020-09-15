while True:
    try:
        N = int(input())
        seq = 0
        v = 1
        for i in range(N):
            aux = v
            v = v + seq
            seq = aux
            while v % 3 != 0 and str(v).find('3') == -1:
                aux = v
                v = v + seq
                seq = aux
        print(v)
    except EOFError:
        break
