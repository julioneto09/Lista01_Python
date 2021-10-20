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

valor = float(input('Quanto você ganha por hora? '))
horas = float(input('Informe quantas horas trabalhou no mês: '))

bruto = valor*horas

inss = 0.08*bruto
sind = 0.05*bruto
ir = 0.11*bruto
desc = inss+sind+ir
liq = bruto - desc

def r(x) :
    return round(x,2)

print('\nLetra a: Valor Bruto: R$ {}' .format(r(bruto)))
print('\nLetra b: INSS: R$ {}' .format(r(inss)))
print('\nLetra c: Sindicato: R$ {}' .format(r(sind)))
print('\nLetra d: Valor Líquido: R$ {}' .format(r(liq)))
print('\nLetra e: Descontos: R$ {}' .format(r(desc)))
