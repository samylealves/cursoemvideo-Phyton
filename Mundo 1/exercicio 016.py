#import math
#n = int(input('Digite o número que deseja saber a raiz:'))
#r = math.sqrt(n)
#print('A raiz de {} é {}'.format(n,math.ceil(r)))

from math import trunc
n = float(input('Digite um valor fracionado:'))
print( 'O número fracionado é {} e a sua porção inteira ficará {}!'.format(n,trunc(n)))
