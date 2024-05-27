nota1 = float(input('Digite sua primeira nota:'))
nota2 = float(input('Digite sa segunda nota:'))
media = (nota1 + nota2)/2
if media > 7:
    print('Tirando {} e {}, sua média fica \33[32m{}\33[m.'.format(nota1,nota2,media))
    print('Parabèns, você esta \33[32mAPROVADO\33[m!!')
elif media < 5:
    print('Tirando {} e {}, sua média fica \33[31m{}\33[m.'.format(nota1,nota2,media))
    print('Você está \33[31mREPROVADO\33[m, estude mais na próxima.')
elif media >= 5 and media < 7 :
    print('Tirando {} e {}, sua média fica \33[33m{}\33[m.'.format(nota1,nota2,media))
    print('Você está de \33[33mRECUPERAÇÃO\33[m, estude para recuperar sua média')