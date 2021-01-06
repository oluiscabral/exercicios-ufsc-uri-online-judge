def get_pair_cards(card, extra):
    ret = [card, card, extra]
    ret.sort()
    return ret


def handle_triple(card):
    if card == 13:
        return None
    else:
        return [card + 1 for i in range(3)]


def handle_pair(card, cards):
    sub = None
    for c in cards:
        if c != card:
            if c == 12 and card == 13:
                return [1, 1, 1]
            if c == 13:
                return get_pair_cards(card+1, 1)
            if c + 1 == card:
                sub = card + 1
            else:
                sub = c + 1
            break
    return get_pair_cards(card, sub)


def handle_none():
    return [1, 1, 2]


def get_next_sequence(cards):
    ret = ''
    sequence = None

    a = cards[0]
    a_count = cards.count(a)
    if a_count == 3:
        sequence = handle_triple(a)
    elif a_count == 2:
        sequence = handle_pair(a, cards)
    elif cards.count(cards[1]) == 2:
        sequence = handle_pair(cards[1], cards)
    else:
        sequence = handle_none()

    if sequence is None:
        return '*'
    return ' '.join(map(str, sequence))


while True:
    cards = [int(w) for w in input().split()]
    if not any(cards):
        break
    print(get_next_sequence(cards))
