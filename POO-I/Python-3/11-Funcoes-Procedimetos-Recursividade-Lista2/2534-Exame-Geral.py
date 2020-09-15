while True:
    try:
        notes = []
        N, Q = [int(w) for w in input().split()]
        for i in range(N):
            notes.append(int(input()))
        notes.sort(reverse=True)
        for i in range(Q):
            query = int(input()) - 1
            print(notes[query])
    except EOFError:
        break
