from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pessoas in range(1,8):
    nasc = int(input('Em que ano a {}° pessoa nasceu?'.format(pessoas)))
    idade = atual - nasc
    if idade < 18:
        totmenor = totmenor + 1
    elif idade >= 18:
        totmaior = totmaior + 1
print('Ao todo tivemos {} menores de idade'.format(totmenor))
print('E também tivemos {} maiores de idade'.format(totmaior))






