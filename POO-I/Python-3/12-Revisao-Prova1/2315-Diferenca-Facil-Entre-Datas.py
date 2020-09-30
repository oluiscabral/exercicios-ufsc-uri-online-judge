import datetime

first = [int(w) for w in input().split()]
second = [int(w) for w in input().split()]

first_date = datetime.date(1, first[1], first[0])
second_date = datetime.date(1, second[1], second[0])

diff = (second_date - first_date).days

print(diff)
