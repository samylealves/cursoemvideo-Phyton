soma = 0
cont = 0
for c in range(1,7):
    n = int(input('Digite o {}º valor:'.format(c)))
    if n % 2 == 0:
        soma = soma + n
        cont = cont + 1
print('Você informou {} números pares e a soma dos valores é {}'.format(cont,soma))
