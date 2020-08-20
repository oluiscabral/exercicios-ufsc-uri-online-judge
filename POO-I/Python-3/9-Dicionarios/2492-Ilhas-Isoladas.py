T = int(input())

while T != 0:
    left = []
    right = []
    isFunction = True
    isInvertible = True
    for i in range(T):
        leftInput, rightInput = input().split(" -> ")
        if isFunction and left.count(leftInput) < 1:
            left.append(leftInput)
        else:
            isFunction = False

        if isInvertible and right.count(rightInput) < 1:
            right.append(rightInput)
        else:
            isInvertible = False
    if not isFunction:
        print("Not a function.")
    elif not isInvertible:
        print("Not invertible.")
    else:
        print("Invertible.")

    T = int(input())
