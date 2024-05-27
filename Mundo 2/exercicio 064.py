'''cont = -1
acumulador = -999
num = 0
while num != 999:
    num = int(input('Digite um número [999 para parar]:'))
    cont = cont + 1
    acumulador = acumulador + num
print('{} números foram lidos e a soma deles é {}'.format(cont, acumulador))
print('Acabou')'''


#OUTRA FORMA
cont = 0
acumulador = 0
num = int(input('Digite um número [999 para parar]:'))
while num != 999:
    cont = cont + 1
    acumulador = acumulador + num
    num = int(input('Digite um número [999 para parar]:'))
print('{} números foram lidos e a soma deles é {}'.format(cont, acumulador))
print('Acabou')
