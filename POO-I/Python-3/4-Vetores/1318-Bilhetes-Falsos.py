N, M = [int(x) for x in input().split()]

while N != 0 or M != 0:
    T = [int(x) for x in input().split()]

    repeatedTickets = []

    for ticket in T:
        if T.count(ticket) > 1 and repeatedTickets.count(ticket) == 0:
            repeatedTickets.append(ticket)

    print(len(repeatedTickets))

    N, M = [int(x) for x in input().split()]
