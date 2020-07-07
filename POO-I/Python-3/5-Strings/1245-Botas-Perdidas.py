while True:
    try:
        N = int(input())
        leftBoots = []
        rightBoots = []
        boots = []
        pairs = 0
        for i in range(N):
            M, L = [x for x in input().split()]
            if boots.count(M) == 0:
                boots.append(M)
            if L == 'E':
                leftBoots.append(M)
            else:
                rightBoots.append(M)
        for b in boots:
            lCount = leftBoots.count(b)
            rCount = rightBoots.count(b)
            if lCount > rCount:
                pairs += lCount - (lCount-rCount)
            else:
                pairs += rCount - (rCount-lCount)
        print(pairs)
    except EOFError:
        break
