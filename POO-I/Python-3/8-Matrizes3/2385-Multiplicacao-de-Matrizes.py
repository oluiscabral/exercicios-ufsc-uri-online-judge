N = int(input())
P, Q, R, S, X, Y = [int(w) for w in input().split()]
I, J = [int(w) for w in input().split()]

lineA = [((P * I + Q * (w+1)) % X) for w in range(N)]
columnB = [((R * (w+1) + S * J) % Y) for w in range(N)]

Cij = sum(map(lambda x, y: x * y, lineA, columnB))
print(Cij)
