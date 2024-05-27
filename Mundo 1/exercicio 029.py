velocidade = float(input('Que velocidade seu carro estava: '))
if velocidade>80:
    print('MULTADO, você excedeu o limite de velocidade permitido que é de 80Km/h')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
else:
    print('Tenha um bom dia, dirija com segurança!')