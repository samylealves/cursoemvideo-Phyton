from time import sleep
v1 = int(input('Primeiro valor:'))
v2 = int(input('Segundo valor:'))
opcao = 0
while opcao != 5:
    print('-=-' * 8)
    print('''   [1] somar
   [2] multiplicar
   [3] maior
   [4] novos números
   [5] sair do programa''')
    opcao = int(input('Qual é a sua opção?'))
    print('-==' * 8)
    if opcao == 1:
        soma = v1 + v2
        print(' A soma entre {} e {} é {}'.format(v1, v2, soma))
    elif opcao == 2:
        multiplicacao = v1*v2
        print('A multiplicação entre {} e {} é {}'.format(v1, v2, multiplicacao))
    elif opcao == 3:
        if v1 > v2:
            print('Entre {} e {} o maior valor é {} '.format(v1, v2, v1))
        elif v2 > v1:
            print('Entre {} e {} o maior valor é {}'.format(v1, v2, v2))
        else:
            print('Eles tem o mesmo valor')
    elif opcao == 4:
        print('Informe os valores novamente:')
        v1 = int(input('Primeiro valor:'))
        v2 = int(input('Segundo valor:'))
    elif opcao == 5:
        print('Finalizando...')
    sleep(2)
print('Fim do programa! Volte sempre!')


