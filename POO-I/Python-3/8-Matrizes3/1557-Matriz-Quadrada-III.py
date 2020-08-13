N = int(input())

while N != 0:
    r = 0
    result = ""
    justifyWidth = len(str((2**(N-1))**2))
    for i in range(N):
        for j in range(N):
            r = 2 ** i * 2 ** j
            result += str(r).rjust(justifyWidth) + " "
        result = result[:-1] + "\n"
    print(result)
    N = int(input())
