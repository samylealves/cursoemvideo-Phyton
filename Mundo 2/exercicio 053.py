frase = str(input('Digite a frase:')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso = inverso + junto[letra]
print('O inverso de {} é {}'.format(junto,inverso))
if junto == inverso:
    print('Temos um palídromo!')
else:
    print('A frase digitada não é um palídromo.')

#OUTRA FORMA
frase = str(input('Digite a frase:')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
if junto == inverso:
    print('Temos um palídromo!')
else:
    print('A frase digitada não é um palídromo.')





