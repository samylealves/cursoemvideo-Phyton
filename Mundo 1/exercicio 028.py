"""import random
lista = [1,2,3,4,5]
escolhido = random.choices(lista)
print('--+'*20)
print('Vou pensar em um número de 1 a 5, tente adivinhar se for capaz:)')
print('--+'*20)
v = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
if v==escolhido:
    print('Parabéns você acertou!')
else:
    print('GANHEI, eu pensei no número {} não o {}!'.format(escolhido,v))"""


#OUTRA FORMA
from random import randint
from time import sleep
computador = randint(0,5)#Faz o computador 'PENSAR'
print('-=-'*20)
print('Vou pensar em um número de 0 a 5. Tente adivinhar...')
print('-=-'*20)
sleep(2)
jogador = int(input('Em que número eu pensei? '))#Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('PARABÉNS, Avocê conseguiu me ganhar!')
else:
    print('GANHEI, eu pensei no número {} não no {}  ;) '.format(computador,jogador))


