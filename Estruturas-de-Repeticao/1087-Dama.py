dama = [int(i) for i in input().split()]

while dama[0] != 0 and dama[1] != 0 and dama[2] != 0 and dama[3] != 0:
    if dama[0] == dama[2] and dama[1] == dama[3]:
        print("0")
    else:
        if dama[0] == dama[2] or dama[1] == dama[3] or ((dama[0] - dama[2])**2)**0.5 == ((dama[1] - dama[3])**2)**0.5:
            print("1")
        else:
            print("2")

    dama = [int(i) for i in input().split()]