'''
Escreva um programa que solicite 2 números inteiros e 1 número real. Calcule e
imprima:
a) o produto do dobro do primeiro número com a metade do segundo número.
b) a soma do triplo do primeiro número com o terceiro número.
c) o terceiro número elevado ao cubo.
'''

x = int(input('Informe um número inteiro: '))
y = int(input('Informe outro número inteiro: '))
z = float(input('Informe um número real:  '))

dobro_x = 2*x
metade_y = y/2
triplo_x = 3*x
cubo_z = pow(z, 3)

a = dobro_x*metade_y
b = triplo_x+z
c = cubo_z

print('\nLetra a: {}\nLetra b: {}\nLetra c: {:f}'.format(a,b,c))


