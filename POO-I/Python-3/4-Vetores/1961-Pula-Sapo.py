P, N = [int(x) for x in input().split()]

h = [int(x) for x in input().split()]

win = True
for i in range(1, N):

    if P < ((h[i] - h[i - 1])**2)**0.5:
        win = False
        break

if win:
    print("YOU WIN")
else:
    print("GAME OVER")
