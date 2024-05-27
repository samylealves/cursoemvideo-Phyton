print('='*25)
print('  10 TERMOS DE UMA PA')
print('='*25)

num = int(input('Primeiro termo:'))
raz = int(input('Razão:'))
dec = num + (10-1) * raz #CALCULAR 10° TERMO

for c in range(num,dec + raz,raz):
    print(c, end=' -> ')
print('ACABOU')
