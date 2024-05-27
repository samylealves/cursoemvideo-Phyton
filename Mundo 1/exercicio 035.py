print('-=-'*10)
print('   Analisador de Triângulos ')
print('-=-'*10)

a = float(input('Primeiro seguimento:'))
b = float(input('Segundo seguimento:'))
c = float(input('Terceiro seguimento:'))

if a < b + c and b < a + c and c < a + b:
    print('Os seguimentos acima PODEM formar um triângulo')
else:
    print('Os seguimentos acima NÃO PODEM formar um triângulo')


