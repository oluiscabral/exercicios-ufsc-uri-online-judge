N = int(input())

for i in range(N):

    D = []
    dado = True

    D.append(int(input()))

    D.extend([int(x) for x in input().split()])

    D.append(int(input()))

    for z in range(1, 7):
        if D.count(z) != 1:
            dado = False
            break
        
    if dado:
        if D[0] + D[5] != 7 or D[1] + D[3] != 7 or D[2] + D[4] != 7:
            dado = False

    if dado:
        print("SIM")
    else:
        print("NAO")