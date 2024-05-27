import math
n = float(input('Digite o valor do seu ângulo:'))
s = math.sin(math.radians(n))
c = math.cos(math.radians(n))
t = math.tan(math.radians(n))
print(' seno:{:.2f}\n cosseno:{:.2f}\n tangente:{:.2f}'.format(s,c,t))