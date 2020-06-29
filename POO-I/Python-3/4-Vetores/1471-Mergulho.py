while True:
    try:
        N, R = [int(x) for x in input().split()]

        returned = [int(x) for x in input().split()]

        notReturned = []

        for i in range(1, N+1):
            if returned.count(i) == 0:
                notReturned.append(i)

        if len(notReturned) != 0:
            for v in notReturned:
                print(v, end=" ")
        else:
            print("*", end="")

        print("")
    except EOFError:
        break
