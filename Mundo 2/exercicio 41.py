from datetime import date
atual = date.today().year
nasc = int(input('Digite o seu ano de nascimento:'))
idade = atual - nasc

if idade <= 9:
    print('O atleta se enquadra na categoria: MIRIM')
elif idade <= 14:
    print('O atleta se enquadra na categoria: INFANTIL')
elif idade <= 19:
    print('O atleta se enquadra na categoria: JUNIOR')
elif idade <= 25:
    print('O atleta se enquadra na categoria: SENIOR')
else:
    print('O atleta se enquadra na categoria: MASTER')