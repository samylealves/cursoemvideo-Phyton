'''print('='*30)
print('{:^30}'.format('BANCO CV'))
print('='*30)
num = int(input('Qual valor você quer sacar? R$'))
total = num
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10'''

for c in range(0,10,3):
    print(c)