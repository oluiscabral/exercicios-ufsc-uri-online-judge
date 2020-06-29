N = int(input())

answerLetters = ['A', 'B', 'C', 'D', 'E']
while N != 0:
    for i in range(N):
        A, B, C, D, E = [int(x) for x in input().split()]
        answers = []

        for answerColor in [A, B, C, D, E]:
            if answerColor <= 127:
                answers.append(True)
            else:
                answers.append(False)

        validator = False
        answerOffset = 0
        for i in range(len(answers)):
            if answers[i]:
                if not validator:
                    validator = True
                    answerOffset = i
                else:
                    validator = False
                    break

        if validator:
            print(answerLetters[answerOffset])
        else:
            print("*")

    N = int(input())
