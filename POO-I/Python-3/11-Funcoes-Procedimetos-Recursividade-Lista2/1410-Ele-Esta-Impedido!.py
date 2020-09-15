A, D = [int(w) for w in input().split()]
while A != 0 or D != 0:
    attackers = []
    defenders = []
    attackers.extend([int(w) for w in input().split()])
    defenders.extend([int(w) for w in input().split()])
    attackers.sort()
    defenders.sort()

    offside = False
    if attackers[0] < defenders[1]:
        offside = True

    if offside:
        print('Y')
    else:
        print('N')

    A, D = [int(w) for w in input().split()]
