print('='*25)
print('\33[32m      LOJAS SAMYLE\33[m')
print('='*25)

preco = float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO\n[1] à vista dinheiro/cheque\n[2] débito\n[3] 2x no cartão\n[4] 3x ou mais no cartão\n')
pagamento = int(input('Qual será a forma de pagamento?'))

if pagamento == 1:
    escolha = preco - preco * (10 / 100)
    print('Você recebeu 10% de desconto em suas compras, você pagará apenas R${:.2f}'.format(escolha))
elif pagamento == 2:
    escolha = preco - preco * (5/100)
    print('Você recebeu desconto de 5% nas suas compras, você pagará R${:.2f}'.format(escolha))
elif pagamento == 3:
    parcelamento = int(input('Quantas Parcelas?'))
    par = preco / parcelamento
    print('Sua compra será parcelada em {}x de {:.2f} SEM JUROS'.format(parcelamento,par))
    print('Suas compras não receberam desconto, vai custar R${:.2f} no final.'.format(preco))
elif pagamento == 4:
    escolha = preco * (20/100) + preco
    parcelamento = int(input('Quantas Parcelas?'))
    par = escolha/parcelamento
    print('Sua compra será parcelada em {}x de {:.2f} COM JUROS'.format(parcelamento,par))
    print('Você recebeu juros de 20% em suas compras, vai custar R${:.2f} no final.'.format(escolha))
else:
    print('\33[31mOPÇÃO INVÁLIDA. digite um número da tabela.\33[m')

