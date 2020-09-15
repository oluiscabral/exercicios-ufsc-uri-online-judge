instance = 1
while True:
    try:
        lowestGrade = None  # [name, grade]
        N = int(input())
        for i in range(N):
            grade = input().split()
            grade[1] = int(grade[1])
            if lowestGrade == None or grade[1] < lowestGrade[1] or (grade[1] == lowestGrade[1] and grade[0] > lowestGrade[0]):
                lowestGrade = grade
        print("Instancia " + str(instance))
        print(lowestGrade[0], end="\n\n")
        instance += 1
    except EOFError:
        break
