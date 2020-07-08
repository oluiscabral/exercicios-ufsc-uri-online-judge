N = int(input())

while N != 0:
    M = [[] for x in range(N)]

    xx = 10

    str(xx).rjust(3)

    half = int(N/2)

    for w in range(2):
        for i in range(int(half)):
            for j in range(i):
                M[i].append(j+1)

            for z in range(i, N - i):
                M[i].append(i + 1)

            for j in range(i, 0, -1):
                M[i].append(j)
        M.reverse()

    if N % 2 != 0:
        for i in range(half):
            M[half].append(i + 1)

        for i in range(half + 1, 0, -1):
            M[half].append(i)

    for i in range(N):
        printable = ""
        for n in M[i]:
            printable += str(n).rjust(3) + " "
        printable = printable.rstrip()
        print(printable)

    print("")

    N = int(input())
