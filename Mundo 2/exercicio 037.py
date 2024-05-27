from time import sleep
num = int(input('Digite um número inteiro:'))

print('Escolha a base de conversão:')
sleep(2)
print('[1] converter para BINÁRIO\n[2] converter para OCTAL\n[3] converter para HEXADECIMAL')

escolha = int(input('Sua escolha:'))

if escolha == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num,bin(num)[2:]))
elif escolha == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num,oct(num)[2:]))
elif escolha == 3:
    print('{} conertido para HEXADECIMAL é igual a {}'.format(num,hex(num)[2:]))
else:
    print('Opção inválida, tente novamente ;)')
