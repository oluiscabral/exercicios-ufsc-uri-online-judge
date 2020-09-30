O, B, I = [float(w) for w in input().split()]

rank = [O, B, I]
rank.sort()

if rank[0] == rank[1]:
    print("Empate")
elif rank[0] == O:
    print("Otavio")
elif rank[0] == B:
    print("Bruno")
else:
    print("Ian")
