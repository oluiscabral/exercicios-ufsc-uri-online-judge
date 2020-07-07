D, N = [int(x) for x in input().split()]

while D != 0 or N != 0:
    result = 0
    strResult = ""

    for strPart in str(N).split(str(D)):
        strResult += strPart

    if strResult.strip() != "":
        result = int(strResult)

    print(result)

    D, N = [int(x) for x in input().split()]
