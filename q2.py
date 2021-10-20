'''
Escreva uma expressão para determinar se uma pessoa deve ou não pagar imposto.
Considere que pagam imposto cujo salário é maior que R$1.200.
'''
valor = 1200
salario = float(input('Informe seu salario em R$: '))

if salario > valor :
    print('\nSeu salário é maior que R$ 1200,00.\nVocê precisa pagar imposto.')
else :
    print ('\nSeu salário é menor ou igual a R$ 1200,00.\nVocê não precisa pagar imposto.')