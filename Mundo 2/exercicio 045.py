from time import sleep
from random import randint
itens = ('Pedra','Papel','Tesoura')
computador = randint(0,2)

print('''Suas oções:
[0] PEDRA
[1] PAPEL
[2] TESOURA ''')
jogador = int(input('Qual sua jogada?'))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)

print('-=-'*10)
print('O COMPUTADOR jogou {}'.format(itens[computador]))
print('O JOGADOR jogou {}'.format(itens[jogador]))
print('-=-'*10)

if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR PERDE')
    else:
        print('\33[31mJOGADA INVÁLIDA\33[m')


elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('\33[31mJOGADA INVÁLIDA\33[m')

elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador ==2:
        print('EMPATE')
    else:
        print('\33[31mJOGADA INVÁLIDA\33[m')








"""if jogador == computador:
    print('Droga,EMPATAMOS.')
elif jogador == 0 and computador == 2:
    print('VOCÊ VENCEU')
elif jogador == 1 and computador == 0:
    print('VOCÊ VENCEU')
elif jogador == 2 and computador == 1:
    print('VOCÊ VENCEU')
elif computador == 0 and jogador == 2:
    print('VOCÊ PERDEU, COMPUTADOR GANHOU')
elif computador == 1 and jogador == 0:
    print('VOCÊ PERDEU, COMPUTADOR GANHOU')
elif computador == 2 and jogador ==1:
    print('VOCÊ PERDEU, COMPUTADOR GANHOU')
else:
    print('\33[31mNÚMERO INVALIDO. Digite um número da tabela para jogarmos.\33[m')""" #Outra forma de fazer



