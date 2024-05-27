peso =float(input('Qual o seu peso? (Kg) '))
altura = float(input('Qual sua altura? (m) '))
imc = peso / (altura**2)
print('Seu IMC é de {:.2f}'.format(imc))
if imc < 18.5:
    print('ABAIXO DO PESO')
elif imc >= 18.5 and imc < 25:
    print('PESO IDEAL')
elif imc >=25 and imc < 30:
    print('ACIMA DO PESO')
elif imc >=30 and imc < 40:
    print('OBESIDADE')
else:
    print('OBESIDADE MÓRBIDA')
