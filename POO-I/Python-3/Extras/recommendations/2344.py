N = int(input())

if N < 1:
    print('E')
elif N < 36:
    print('D')
elif N < 61:
    print('C')
elif N < 86:
    print('B')
else:
    print('A')
