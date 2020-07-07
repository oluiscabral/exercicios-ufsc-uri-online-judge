algarism_leds = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

N = int(input())

for i in range(N):
    number = input()
    result = 0

    for algarism in number:
        result += algarism_leds[int(algarism)]

    print(str(result) + " leds")
