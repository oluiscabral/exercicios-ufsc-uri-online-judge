while True:
    try:
        h, m = [int(w) for w in input().split()]
        print(f'{h // 30:02d}:{m // 6:02d}')
    except EOFError:
        break
