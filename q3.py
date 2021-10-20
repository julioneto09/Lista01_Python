'''
Escreva um programa que solicite 2 números inteiros e 1 número real. Calcule e
imprima:
a) o produto do dobro do primeiro número com a metade do segundo número.
b) a soma do triplo do primeiro número com o terceiro número.
c) o terceiro número elevado ao cubo.
'''
import math

x = input('Informe um número inteiro: ')
y = input('Informe outro número inteiro: ')
z = input('Informe um número real:  ')

dobro = 2*int(x)
metade = int(y)/2
triplo = 3*int(x)
cubo = math.pow(float(z),3)
#cubo = pow(float(z), 3)

a = dobro*metade
b = triplo+float(z)
c = cubo

print('\nLetra a: %f\nLetra b: %f\nLetra c: %f' %(a, b, c))


