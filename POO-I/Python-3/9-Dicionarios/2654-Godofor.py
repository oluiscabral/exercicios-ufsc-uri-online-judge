N = int(input())

strongest = {}

for i in range(N):
    S, P, K, M = input().split()
    P, K, M = [int(w) for w in [P, K, M]]
    greater = False
    if strongest.get('name', False):
        if P == strongest.get('power'):
            if K == strongest.get('kills'):
                if M == strongest.get('deaths'):
                    if S < strongest.get('name'):
                        greater = True
                elif M < strongest.get('deaths'):
                    greater = True
            elif K > strongest.get('kills'):
                greater = True
        elif P > strongest.get('power'):
            greater = True
    else:
        greater = True

    if greater:
        strongest['name'] = S
        strongest['power'] = P
        strongest['kills'] = K
        strongest['deaths'] = M

print(strongest['name'])
