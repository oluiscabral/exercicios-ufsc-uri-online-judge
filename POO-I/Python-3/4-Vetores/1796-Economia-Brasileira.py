Q = int(input())

V = [int(x) for x in input().split()]

satisfactory = 0
for v in V:
    if v == 0:
        satisfactory += 1

if satisfactory > Q / 2:
    print("Y")
else:
    print("N")
