while True:
    try:
        N = int(input())

        nMain = N // 3
        nCenter = nMain + N % 3
        nHalf = nCenter // 2

        decoration = ""
        middle = ""
        reversedDecoration = ""

        # output is going to be equal decoration + middle + reversedDecoration
        output = ""

        # let's get decoration first
        for i in range(nMain):
            decoration += "2".rjust(i+1, '0') + "0" * (N - 2 *
                                                       (i+1)) + "3".ljust(i+1, '0') + '\n'

        # I could iterate line using reversed() and concat reversedDec within a reversed line...
        # but hardcoding it like this has a better execution run time
        for i in range(nMain-1, -1, -1):
            reversedDecoration += "3".rjust(i+1, '0') + "0" * (N - 2 *
                                                               (i+1)) + "2".ljust(i+1, '0') + '\n'

        # getting the middle done:
        middle = (("1" * nCenter).center(N, '0') + '\n') * (nHalf)
        if N % 2 != 0:
            middle += ("1" * nHalf + "4" + "1" * nHalf).center(N, '0') + '\n'
        middle += (("1" * nCenter).center(N, '0') + '\n') * (nHalf)

        output = decoration + middle + reversedDecoration

        print(output)
    except EOFError:
        break
