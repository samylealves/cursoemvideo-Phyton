#co = float(input('Digite o comprimento do cateto oposto:'))
#ca = float(input('Digite o comprimento do cateto adjacente:'))
#h = (co**2 + ca**2)**(1/2)
#print('o valor da hipotenusa é {:.2f}'.format(h))
import math
co = float(input('Digite o comprimento do cateto oposto:'))
ca = float(input('Digite o comprimento do cateto adjacente:'))
h = math.hypot(co,ca)
print('O valor da hipotenusa é de {:.2f}!'.format(h))
