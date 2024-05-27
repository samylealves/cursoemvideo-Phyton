vcasa = float(input('Qual o valor da casa que pretende comprar: R$'))
salario = float(input('Qual o seu salário: R$'))
anos = float(input('Quantos anos de financiamento? '))

prestacao = vcasa/(anos*12)

print('-=-'*25)
print('Para pagar uma casa de \33[32mR${}\33[m em \33[32m{} anos\33[m '.format(vcasa,anos),end='')
print('a prestação será de \33[32mR${:.2f}\33[m'.format(prestacao))
print('-=-'*25)

minimo = salario * (30/100)
if prestacao<= minimo:
    print('\33[32mEMPRESTIMO CONCEDIDO!\33[m')
else:
    print('\33[31mEMPRESTIMO NEGADO, a prestaçõa excede 30% do seu salário!\33[m')
