'''
Escreva um programa que pede o dia do mês e o dia da semana em que você irá entrar
de férias e ediaibe o dia da semana que você voltará a trabalhar. Ediaemplo, você terá umas
férias maravilhosas que começam no dia 3, quarta-feira e retornará das suas férias
depois de 137 noites.
'''
print('\nDias da semana: \tdomingo, segunda, terça, quarta, quinta, sexta, sábado\n\n')
data = int(input('Informe a data do início das férias: '))
dia = input('Informe qual dia da semana inicia as férias: ')
#dia = dia.lower()
tempo = int(input('Informe quantos dias de férias: '))


def dias(x) :
    if x == 'domingo':  
        a = 1  
    elif x == 'segunda':    
        a = 2
    elif x == 'terça':    
        a = 3
    elif x == 'quarta':    
        a = 4
    elif x == 'quinta':    
        a = 5
    elif x == 'sexta':    
        a = 6
    elif x == 'sábado' :
        a = 7
    else :
        print ('\nDia da semana inválido!\nO programa será encerrado...')
        return exit()
    
    return a

def datas(y) :
    if y == 1:  
        b = 'domingo'  
    elif y == 2:    
        b = 'segunda'
    elif y == 3:    
        b = 'terça'
    elif y == 4:    
        b = 'quarta'
    elif y == 5:    
        b = 'quinta'
    elif y == 6:    
        b = 'sexta'
    elif y == 7:
        b = 'sábado'
    else :
        return ()
    return b

resto = tempo%7

if (dias(dia)+resto+1) <= 7 :
    volta = datas(dias(dia)+resto)

else :
    volta = datas(dias(dia)+resto-7)

print('\nVocê volta no(a) %s, dia %d' %(volta, data+tempo))