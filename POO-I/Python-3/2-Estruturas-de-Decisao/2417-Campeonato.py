Cv, Ce, Cs, Fv, Fe, Fs = [int(x) for x in input().split()]

pontos_C = Cv * 3 + Ce
pontos_F = Fv * 3 + Fe

if pontos_C == pontos_F:
    if Cs == Fs:
        print("=")
    elif Cs > Fs:
        print("C")
    else:
        print("F")
elif pontos_C > pontos_F:
    print("C")
else:
    print("F")