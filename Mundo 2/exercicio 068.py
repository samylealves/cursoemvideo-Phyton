from random import randint
print('-=-'*10)
print('  VAMOS JOGAR PAR OU ÍMPAR')
print('-=-'*10)
cont = 0
while True:
    jogador = int(input('Diga um valor:'))
    computador = randint(0, 10)
    escolha = str(input('Par ou Ímpar? [P/I]')).strip().upper()[0]
    soma = computador + jogador
    print('___'*16)
    print(f'Você jogou {jogador} e o computador {computador}. O total deu {soma}', end=' ')
    print('DEU PAR'if soma % 2 == 0 else 'DEU ÍMPAR')
    print('___'*16)
    if escolha == 'P':
        if soma % 2 == 0:
            print('VOCÊ GANHOU')
            cont = cont + 1
        else:
            print('VOCÊ PERDEU')
            break
    if escolha == 'I':
        if soma % 3 == 0:
            print('VOCÊ GANHOU')
            cont = cont + 1
        else:
            print('VOCÊ PERDEU')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {cont} vezes. ')
