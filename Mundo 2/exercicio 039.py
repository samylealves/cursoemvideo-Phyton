from datetime import date
atual = date.today().year

sexo = int(input('[1] Masculino\n[2] Feminino\nDigite seu sexo:'))
if sexo == 2:
    print('O alistamento obrigátorio no Brasil , é apenas para homens, obrigada.')

else:
    print('-=-'*10)
    print('Bem vindo a sua consulta de alistamento!')

    nasc = int(input('Informe o ano do seu nascimento:'))
    print('-=-'*10)

    idade = atual - nasc
    print('Quem nasceu em {} tem {} anos em {}'.format(nasc,idade,atual))

    if idade == 18:
        print('É hora de se alistar, você tem 18 anos:')
    elif idade > 18:
        saldo = idade - 18
        alis = atual - saldo
        print('Já se passou o periodo de seu alistamento, já se passaram {} anos.'.format(saldo))
        print('Seu alistamento foi em {}'.format(alis))
    elif idade< 18:
        saldo = 18 - idade
        alis = atual + saldo
        print('Você ainda vai se alistar, faltam {} anos para seu alistamento.'.format(saldo))
        print('Seu alistamento será em {}'.format(alis))

