while True:
    try:
        A, B, C = [bool(int(x)) for x in input().split()]

        if all([A, B, C]) or not any([A, B, C]):
            print("*")
        else:
            if sum(i == True for i in [A, B, C]) == 1:
                comparator = True
            else:
                comparator = False

            if A == comparator:
                    print("A")
            else:
                if B == comparator:
                    print("B")
                else:
                    print("C")

    except EOFError:
        break
