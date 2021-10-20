'''
Faça uma lista que simule uma pilha de pratos.
'''

a = input('informe um elemento: ')
b = input('informe outro elemento: ')
c = input('informe outro elemento: ')

pilha = ['nome', 10, True]

pilha.append(a)
pilha.append(b)
pilha.append(c)

print(pilha)
comp = len(pilha)

x = int(input('\ninforme quantos elementos quer excluir: '))
i = 1

if x <= comp :
    while comp-x < len(pilha) :    
        print('\nExcluindo o %d° elemento' %(i))
        i += 1
        pilha.pop()
        print(pilha)
        
else:
    print('\nA pilha tem menos elementos do que você quer excluir!')
    exit