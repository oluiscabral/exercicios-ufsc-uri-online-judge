N, M = [int(x) for x in input().split()]

while N != 0 or M != 0:
    answers = []
    resolvedCount = [0 for x in range(M)]
    notResolvedCount = [0 for x in range(M)]

    noAllResolvedByOne = True
    allResolved = True
    noOneAllResolved = True
    atLeastOne = True

    score = 0

    for i in range(N):
        answers.append([int(x) for x in input().split()])

        # 1
        if all(answers[-1]):
            noAllResolvedByOne = False

        # 4
        if not any(answers[-1]):
            atLeastOne = False

        for z in range(M):
            if answers[-1][z] == 1:
                resolvedCount[z] += answers[-1][z]
            else:
                notResolvedCount[z] += answers[-1][z]

    # 2
    if not all(resolvedCount):
        allResolved = False

    # 3
    if resolvedCount.count(N) > 0:
        noOneAllResolved = False

    # score counter
    if noAllResolvedByOne:
        score += 1

    if allResolved:
        score += 1

    if noOneAllResolved:
        score += 1

    if atLeastOne:
        score += 1

    print(score)

    N, M = [int(x) for x in input().split()]
