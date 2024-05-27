print('Gerador de PA')
print('-==-'*5)

num = int(input('Primeiro termo:'))
raz = int(input('Razão:'))
termo = num
cont = 1

while cont<= 10:
    print('{} -> '.format(termo), end='')
    cont = cont + 1
    termo = termo + raz
print('FIM ')
