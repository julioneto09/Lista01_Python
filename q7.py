'''
Escreva um programa que leia 2 strings e informe o conteúdo e o comprimento de cada
uma delas. Informe também se as duas strings possuem o mesmo comprimento e se
apresentam o mesmo conteúdo.
'''

a = input('Escreve alguma coisa: ')
b = input('Escreve alguma coisa: ')

comp_a = len(a)
comp_b = len(b)

print("A primeira coisa escrita foi: '%s', e seu comprimento é %d" %(a, comp_a))
print("A segunda coisa escrita foi: '%s', e seu comprimento é %d" %(b, comp_b))

a = a.strip().lower()
b = b.strip().lower()

i = 0

while i < comp_a :
    if a[i] == b[i] :
        i += 1
    else :
        break
if i == comp_a :
    print('o conteudo das duas strings é igual')
else:
    print('o conteudo das duas strings é diferente')