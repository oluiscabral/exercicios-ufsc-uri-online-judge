notes = {
    'W': 1,
    'H': 1/2,
    'Q': 1/4,
    'E': 1/8,
    'S': 1/16,
    'T': 1/32,
    'X': 1/64
}

I = input()

while I != '*':
    noteSum = 0
    partialSum = 0
    for unit in I[1:]:
        if unit == '/':
            if partialSum == 1:
                noteSum += 1
            partialSum = 0
            continue
        partialSum += notes[unit]

    print(noteSum)

    I = input()
