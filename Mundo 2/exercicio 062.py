print('-==-'*6)
print('    Gerador de PA')
print('-==-'*6)

num = int(input('Primeiro termo:'))
raz = int(input('Razão da PA:'))
cont = 1#CONTADOR
termo = num#ACUMULADOR
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:#o cont faz ir de 1 a 10
        print('{} -> '.format(termo), end='')
        termo = termo + raz#FAZ A PA
        cont = cont + 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar mais?'))
print('Progressão finalizada com \33[32m{}\33[m termos mostrados!'.format(total))
print('FIM')