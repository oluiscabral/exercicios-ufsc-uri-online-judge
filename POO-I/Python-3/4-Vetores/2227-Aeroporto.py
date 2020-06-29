A, V = [int(x) for x in input().split()]

testCount = 0
while A != 0 or V != 0:
    testCount += 1

    X, Y = [], []

    flightCount = [int(0) for x in range(A)]
    for i in range(V):
        x, y = [int(x) for x in input().split()]
        flightCount[x-1] += 1
        flightCount[y-1] += 1
        X.append(x)
        Y.append(y)

    topAirports = []
    maxFlights = max(flightCount)
    for i in range(A):
        if flightCount[i] == maxFlights:
            topAirports.append(i + 1)

    print("Teste " + str(testCount))

    topAirportsLen = len(topAirports)
    for i in range(topAirportsLen):
        print(topAirports[i], end=" ")

    print("\n")

    A, V = [int(x) for x in input().split()]
