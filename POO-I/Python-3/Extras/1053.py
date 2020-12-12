def get_invalid_positions(l, c):
    limit = 5
    invalid_positions = []
    for i in range(1, 5):
        var_l = l + i
        var_c = c + i
        if var_l < 5 and var_c < 5:
            invalid_positions.append((var_l, var_c))
        else:
            break
    for i in range(1, 5):
        var_l = l + i
        var_c = c - i
        if var_l < 5 and var_c > -1:
            invalid_positions.append((var_l, var_c))
        else:
            break
    for i in range(1, 5):
        var_l = l - i
        var_c = c + i
        if var_l > -1 and var_c < 5:
            invalid_positions.append((var_l, var_c))
        else:
            break
    for i in range(1, 5):
        var_l = l - i
        var_c = c - i
        if var_l > -1 and var_c > -1:
            invalid_positions.append((var_l, var_c))
        else:
            break
    invalid_positions.extend(get_keys_line_and_column(l, c))
    return invalid_positions


def get_near_valid_positions(l, c):
    valid_positions = []
    directions = [[l, c - 1], [l + 1, c], [l, c + 1], [l - 1, c]]
    for d in directions:
        dL, dC = d[0], d[1]
        if dL >= 0 and dL < 5 and dC >= 0 and dC < 5:
            valid_positions.append((dL, dC))
    return valid_positions


def get_keys_invalid_line_and_column(l, c, keys):
    positions = []
    for i in range(5):
        if i != c:
            positions.append(keys[l][i])
        if i != l:
            positions.append(keys[i][c])
    return positions


keys = [
    [
        (chr(i), j) for j in range(1, 6)
    ] for i in range(65, 70)
]

graphs = {}

for i in range(len(keys)):
    for j in range(5):
        graphs[keys[i][j]] = []
        for k in range()


T = int(input())

N = int(input())
