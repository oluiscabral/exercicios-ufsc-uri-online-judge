def get_key_from_value(value):
    global samples
    for key in samples:
        if samples[key] == value:
            return str(key)


def get_nums():
    global samples, D
    search_codes = [[] for i in range(D)]
    for i in range(2):
        for j, part in enumerate(input().split()):
            search_codes[j].append([1 if w == '*' else 0 for w in part])
    input()
    nums = ''
    for search_code in search_codes:
        nums += get_key_from_value(search_code)
    return nums


def get_code():
    nums = input()
    global samples
    return '\n'.join(
        [' '.join(
            [''.join(['*' if w else '.' for w in samples[int(num)][i]]) for num in nums])
            for i in range(2)]) + '\n' + '.. ' * (len(nums) - 1) + '..'


samples = {
    0: [[0, 1], [1, 1]],
    1: [[1, 0], [0, 0]],
    2: [[1, 0], [1, 0]],
    3: [[1, 1], [0, 0]],
    4: [[1, 1], [0, 1]],
    5: [[1, 0], [0, 1]],
    6: [[1, 1], [1, 0]],
    7: [[1, 1], [1, 1]],
    8: [[1, 0], [1, 1]],
    9: [[0, 1], [1, 0]]
}

while True:
    D = int(input())
    if D == 0:
        break

    S = input()

    if S == 'S':
        print(get_code())
    else:
        print(get_nums())
