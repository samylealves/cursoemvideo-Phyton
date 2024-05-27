print('-=-'*11)
print('    \33[31mAnalisador de Triângulos\33[m')
print('-=-'*11)

a = float(input('Primeiro segmento:'))
b = float(input('Segundo segmento:'))
c = float(input('Terceiro segmento:'))

if a + b > c and a + c > b and b + c > a:
    print('Os segmentos acima FORMAM um triângulo ',end='')
    if a == b == c:
        print('EQUILÁTERO!')
    elif a != b and b != c and c != a:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else :
    print('Os segmentos NÃO FORMAM um triângulo')