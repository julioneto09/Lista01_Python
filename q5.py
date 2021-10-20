'''
Escreva um programa que calcule o aumento de um salário. Ele deve solicitar o valor do
salário e a porcentagem do aumento. Imprima o valor do aumento e do novo salário.
'''

salario = float(input('Informe o salário atual: '))
per = float(input('Informe o percentual de aumento: '))

per /= 100

aumento = salario*per

salario += aumento

print('O aumento foi de R$ %.2f, e o novo salário é R$ %.2f' %(aumento, salario))