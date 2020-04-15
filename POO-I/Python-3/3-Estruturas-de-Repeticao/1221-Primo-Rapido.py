import math

N = int(input())

for i in range(0, N):
    X = int(input())
    
    if X % 2 == 0 and X > 2:
        print("Not Prime")
    else:
        if all(X % z for z in range(3,int(math.sqrt(X))+1, 2)):
            print("Prime")
        else:
            print("Not Prime")