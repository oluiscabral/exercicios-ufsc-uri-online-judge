N = int(input())

A, P, L = [int(x) for x in input().split()]

if N <= A and N <= P and N <= L:
    print("S")
else:
    print("N")