N = int(input())

repetitions = {}

for i in range(N):
    value = int(input())
    if value in repetitions.keys():
        repetitions[value] += 1
    else:
        repetitions[value] = 1

for key in sorted(repetitions.keys()):
    value = repetitions[key]
    print(str(key) + " aparece " + str(value) + " vez(es)")
