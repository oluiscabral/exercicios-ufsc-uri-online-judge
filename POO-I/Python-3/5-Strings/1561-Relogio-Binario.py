presentationSample = """ ____________________________________________
|                                            |
|    ____________________________________    |_
|   |                                    |   |_)
|   |   8         4         2         1  |   |
|   |                                    |   |
|   |   x         x         x         x  |   |
|   |                                    |   |
|   |                                    |   |
|   |   x     x     x     x     x     x  |   |
|   |                                    |   |
|   |   32    16    8     4     2     1  |   |_
|   |____________________________________|   |_)
|                                            |
|____________________________________________|
"""

while True:
    try:
        H, M = [int(x) for x in input().split(':')]

        presentation = presentationSample

        virtualH = H
        for i in range(3, -1, -1):
            ix = 2**i
            z = presentation.find('x')
            if virtualH != 0 and virtualH % ix != virtualH:
                presentation = presentation[:z] + 'o' + presentation[z + 1:]
                virtualH -= ix
            else:
                presentation = presentation[:z] + ' ' + presentation[z + 1:]

        virtualM = M
        for i in range(5, -1, -1):
            ix = 2**i
            z = presentation.find('x')
            if virtualM != 0 and virtualM % ix != virtualM:
                presentation = presentation[:z] + 'o' + presentation[z + 1:]
                virtualM -= ix
            else:
                presentation = presentation[:z] + ' ' + presentation[z + 1:]

        print(presentation, end="\n")

    except EOFError:
        break
