palavra = []
palavra.append(input())
palavra.append(input())
palavra.append(input())

if palavra[0] == "vertebrado":
    if palavra[1] == "ave":
        if palavra[2] == "onivoro":
            print("pomba")
        else:
            print("aguia")
    else:
        if palavra[2] == "onivoro":
            print("homem")
        else:
            print("vaca")
else:
    if palavra[1] == "inseto":
        if palavra[2] == "hematofago":
            print("pulga")
        else:
            print("lagarta")
    else:
        if palavra[2] == "hematofago":
            print("sanguessuga")
        else:
            print("minhoca")