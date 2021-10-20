'''
Escreva um programa que leia 2 strings e informe o conteúdo e o comprimento de cada
uma delas. Informe também se as duas strings possuem o mesmo comprimento e se
apresentam o mesmo conteúdo.
'''

a = input('Escreve alguma coisa: ')
b = input('Escreve alguma coisa: ')

comp_a = len(a)

comp_b = len(b)

print("\nA primeira coisa escrita foi: '%s', e seu comprimento é %d" %(a, comp_a))
print("A segunda coisa escrita foi: '%s', e seu comprimento é %d" %(b, comp_b))
x = comp_a
a = a.strip().lower()
b = b.strip().lower()

'''
Removendo espaços em branco no início e fim das strings, e forçando as duas sentenças a terem apenas caracteres 
minúsculos, para analisar se o conteúdo/mensagem de ambas é o mesmo.'''

i = 0
while i < comp_a :
    if a[i] == b[i] :
        i += 1
    else :
        print ('erro')
        break
if i == comp_a :
    print('\nLogo, o conteúdo das duas strings é igual!')
else:
    print('\nAssim, o conteúdo das duas strings é diferente!')


#Notas mentais
'''
Se a primiera string (a verificação é sobre seu comprimento) tiver espaços vazios no inicio, deu erro.
Apesar da verificação de espaços no vazios no inicio da string, se houver espaços vazios 
no 'meio' da string, mesmo que a mensagem seja a mesma, o código acusará conteúdo diferente.
'''