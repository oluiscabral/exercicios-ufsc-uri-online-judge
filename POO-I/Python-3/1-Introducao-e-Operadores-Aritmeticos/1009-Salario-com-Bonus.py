# -*- coding: utf-8 -*-

nome = input()

salario_fixo = round(float(input()), 2)

total_vendas = round(float(input()), 2)

total = salario_fixo + total_vendas * 0.15

print("TOTAL = R$ {0:.2f}".format(total))