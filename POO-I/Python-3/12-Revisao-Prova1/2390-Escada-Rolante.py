N = int(input())

motion_start = None
motion_end = None
total = 0
for i in range(N):
    x = int(input())
    if motion_start == None:
        motion_start = x
        motion_end = x + 10
    elif x <= motion_end:
        motion_end = x + 10
    else:
        total += motion_end - motion_start
        motion_start = x
        motion_end = x + 10
    if i == N - 1:
        total += motion_end - motion_start
print(total)
