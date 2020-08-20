N = int(input())

while N != 0:
    students = {}
    for i in range(N):
        name, signature = input().split()
        students[name] = signature
    fakeSignatures = 0
    for i in range(int(input())):
        name, signature = input().split()
        dictSignature = students.get(name)
        sigLen = len(signature)
        if sigLen == len(dictSignature):
            diffs = 0
            for i in range(sigLen):
                if signature[i] != dictSignature[i]:
                    diffs += 1
                    if diffs > 1:
                        fakeSignatures += 1
                        break
        else:
            fakeSignatures += 1

    print(fakeSignatures)

    N = int(input())
