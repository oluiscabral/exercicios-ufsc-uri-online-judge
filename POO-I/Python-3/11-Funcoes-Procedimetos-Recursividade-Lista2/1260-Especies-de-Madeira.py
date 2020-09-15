N = int(input())
input()

outer = 0

while outer < N:
    if outer > 0:
        print('')
    outer += 1

    trees = {}
    try:
        inp = input()
        inner = 0
        while inp != '':
            inner += 1
            if inp in trees.keys():
                trees[inp] += 1
            else:
                trees[inp] = 1
            inp = input()
    except:
        pass

    percentages = {}

    for key in trees.keys():
        percentages[key] = (trees[key] / inner) * 100

    keys = list(trees.keys())
    keys.sort()
    for key in keys:
        print(f'{key} {percentages[key]:.4f}')
