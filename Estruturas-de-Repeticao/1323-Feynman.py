N = int(input())

quadrados = N * N

while N != 0:
    for x in range(2, N+1):
        quadrados += (N - x + 1)**2
        
    print(quadrados)
    
    N = int(input())
    quadrados = N * N