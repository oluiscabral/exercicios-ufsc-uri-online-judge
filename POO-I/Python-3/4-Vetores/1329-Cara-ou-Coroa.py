N = int(input())

while N != 0:
    R = [int(x) for x in input().split()]

    johnWins = 0
    maryWins = 0

    for result in R:
        if result == 0:
            maryWins += 1
        else:
            johnWins += 1

    print("Mary won " + str(maryWins) +
          " times and John won " + str(johnWins) + " times")

    N = int(input())
