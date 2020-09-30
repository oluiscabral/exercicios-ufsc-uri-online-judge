R = int(input())

counter = 1
while R != 0:
    aldo_points = 0
    beto_points = 0
    for i in range(R):
        A, B = [int(w) for w in input().split()]
        aldo_points += A
        beto_points += B

    print("Teste " + str(counter))
    if aldo_points > beto_points:
        print("Aldo")
    else:
        print("Beto")
    print('')

    counter += 1
    R = int(input())
