# pega a entrada da distância do corte de B e a distância do corte 7, um em cada linha
B = int(input())
T = int(input())

# armazena os valores da área total da nota
note_area = 70 * 160
# calcula valor da metade da área total da nota
half_note_area = note_area / 2

# calcula a área da parte à esquerda da nota (um trapézio)
left_area = ((B + T) * 70) / 2
# calcula a área à direita da nota
# pega a área total da nota e subtrai pelo trapézio calculado anteriormente
right_area = note_area - left_area

if left_area > half_note_area:
    # a maior parte da nota é a parte esquerda
    print(1)
elif right_area > half_note_area:
    # a maior parte da nota é a parte direita
    print(2)
else:
    # nenhuma das partes é maior que a área da metade da nota
    print(0)
