fun = float(input('Qual o salário do seu funcionário? R$'))
aumento = fun * (15/100) + fun
aumento2 = fun * (10/100) + fun
if fun <= 1250:
    print('Quem ganhava R${} passará a ganhar R${}'.format(fun,aumento))
else:
    print('Quem ganhava R${} passará a ganhar R${}'.format(fun,aumento2))

