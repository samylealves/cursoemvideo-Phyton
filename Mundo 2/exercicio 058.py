from random import randint
computador = randint(0,10)
cont = 1
print('-=-'*13)
print('\33[33mSou seu computador...\33[m')
print('\33[34mAcabei de pensar em um número de 0 a 10.\nSerá que consegue adivinhar qual foi?\33[m')
print('-=-'*13)
palpite = int(input('Qual o seu palpite?'))
while computador != palpite:# OUTRA FORMA ; acertou = False
    if palpite > computador:
        print('Menos... Tente mais uma vez.')
        palpite = int(input('Qual o seu palpite?'))
        cont = cont + 1
    elif palpite < computador:
        print('Mais... Tente mais uma vez.')
        palpite = int(input('Qual o seu palpite? '))
        cont = cont + 1
print('Acertou com {} tentativas.Parabéns!'.format(cont))
