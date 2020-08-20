epr = 0
ehd = 0
intruders = 0


def sumUp(v):
    global epr, ehd, intruders
    if v == 0:
        epr += 1
    elif v == 1:
        ehd += 1
    elif v == 2:
        intruders += 1


registry = {
    'EPR': 0,
    'EHD': 1,
}

while True:
    try:
        for i in range(int(input())):
            sumUp(registry.get((input().split())[1], 2))

        print("EPR: " + str(epr) + "\n" + "EHD: " +
              str(ehd) + "\n" + "INTRUSOS: " + str(intruders))

        epr = 0
        ehd = 0
        intruders = 0
    except EOFError:
        break
