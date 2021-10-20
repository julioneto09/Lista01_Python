'''
Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do
usuário. Calcule e imprima o total em segundos.
'''

dia = int(input('Informe a quantidade de dias: '))
hora = int(input('Informe a quantidade de horas: '))
minuto = int(input('Informe a quantidade de minutos: '))
segundos = int(input('Informe a quantidade de segundos: '))

m = 60
h = 60
d = 24
'''1 minuto (m) tem 60  segundos,
1 hora (h) tem 60 minutos,
e 1 dia (d) tem 24 horas
'''
def m_s(x) :
    return x*m

def h_s(x) :
    return x*h*m

def d_s(x) :
    return x*d*h*m
'''Criando funções para converter minutos em segundos, horas em segundos e dias em segundos
'''
total = m_s(minuto)+h_s(hora)+d_s(dia)+segundos

print('\nO total é de %ds' %total)

