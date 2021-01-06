def get_hailstone_sequence(h: int):
    ret = [h]
    if h == 1:
        return ret
    if h % 2 == 0:
        ret.extend(get_hailstone_sequence(h // 2))
    else:
        ret.extend(get_hailstone_sequence(h * 3 + 1))
    return ret


def get_greatest_from_hailstone_sequence(init: int):
    return max(get_hailstone_sequence(init))


while True:
    H = int(input())
    if H == 0:
        break
    print(get_greatest_from_hailstone_sequence(H))
