'''
Escreva um programa que calcule o aumento de um salário. Ele deve solicitar o valor do
salário e a porcentagem do aumento. Imprima o valor do aumento e do novo salário.
'''

salario = float(input('Informe o salário atual: '))
per = float(input('Informe o percentual de aumento: '))

aumento = salario*(per/100)

salario += aumento

print('\nO aumento foi de R$ %.2f\nO novo salário é R$ %.2f' %(aumento, salario))