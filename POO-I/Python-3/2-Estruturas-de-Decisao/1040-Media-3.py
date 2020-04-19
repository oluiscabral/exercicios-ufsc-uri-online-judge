N1, N2, N3, N4 = [float(x) for x in input().split()]

media = (N1*2 + N2*3 + N3*4 + N4*1) / 10

print("Media: {0:.1f}".format(media))

if media >= 7:
    print("Aluno aprovado.")
elif media < 5:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")

    N_exame = float(input())

    print("Nota do exame: "+ str(N_exame))

    media = (media + N_exame) / 2

    if media >= 5:
        print("Aluno aprovado.")
    else:
        print("Aluno Reprovado.")
    
    print("Media final: {0:.1f}".format(media))