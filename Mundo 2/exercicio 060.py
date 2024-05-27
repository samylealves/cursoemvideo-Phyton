'''from math import factorial
num = int(input('Digite um valor:'))
f = factorial(num)
print('O fatorial de {} é {}.'.format(num,f))'''

num = int(input('Digite um valor:'))
c = num
f = 1
print('Calculando {}!'.format(num))
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f = f * c
    c = c - 1
print('{}'.format(f))

