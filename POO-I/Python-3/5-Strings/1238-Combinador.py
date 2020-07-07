N = int(input())

for i in range(N):
    first_string, second_string = [x for x in input().split()]

    i = 0
    first_string_len = len(first_string)
    second_string_len = len(second_string)

    combination = ""

    while i < first_string_len or i < second_string_len:
        if i < first_string_len:
            combination += first_string[i]

        if i < second_string_len:
            combination += second_string[i]

        i += 1

    print(combination)
