'''
Escreva um programa que pergunte quanto você ganha por hora e o número de horas
trabalhadas no mês. Desta forma, calcule e imprima o total do seu salário no referido
mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e
5% para o sindicato, faça um programa que nos dê (imprima):
a) salário bruto.
b) quanto pagou ao INSS.
c) quanto pagou ao sindicato.
d) o salário líquido.
e) calcule os descontos.
'''

ganho = float(input('Quanto você ganha por hora? '))
horas = float(input('Informe quantas horas trabalhou no mês: '))

bruto = ganho*horas

inss = 0.08*bruto
sind = 0.05*bruto
ir = 0.11*bruto
desc = inss+sind+ir
liq = bruto - desc

print('\nLetra a: Valor Bruto R$ %.2f\nLetra b: INSS R$ %.2f \
    \nLetra c: Sindicato R$ %.2f\nLetra d: Valor Líquido R$ %.2f \
    \nLetra e: Descontos R$ %.2f' %(bruto, inss, sind, liq, desc))

