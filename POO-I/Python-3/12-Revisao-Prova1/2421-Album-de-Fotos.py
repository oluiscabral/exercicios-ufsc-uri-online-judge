X, Y = [int(w) for w in input().split()]

L1, H1 = [int(w) for w in input().split()]
L2, H2 = [int(w) for w in input().split()]

if (((L1 <= X and L2 <= X) and H1+H2 <= Y) or ((L1 <= X and H2 <= X) and H1+L2 <= Y) or ((H1 <= X and L2 <= X) and L1+H2 <= Y) or ((H1 <= X and H2 <= X) and L1+L2 <= Y) or ((L1 <= Y and L2 <= Y) and H1+H2 <= X) or ((L1 <= Y and H2 <= Y) and H1+L2 <= X) or ((H1 <= Y and L2 <= Y) and L1+H2 <= X) or ((H1 <= Y and H2 <= Y) and L1+L2 <= X)):
    print('S')
else:
    print('N')
