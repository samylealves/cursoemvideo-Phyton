print('-'*25)
print('   LOJA SUPER BARATÃO')
print('-'*25)

totcompra = 0
pmaismil = 0
pmaisbarato = 0
nomemaisbarato = ''
cont = 0
while True:
    nome = str(input('Nome do produto:')).strip().capitalize()
    preco = float(input('Preço: R$'))
    totcompra = totcompra + preco
    cont = cont + 1

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if preco > 1000:
        pmaismil = pmaismil + 1
    if cont == 1 or preco < pmaisbarato:
        pmaisbarato = preco
        nomemaisbarato = nome
    if continuar == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${totcompra:.2f}')
print(f'Temos {pmaismil} produto custando mais de R$1000.00')
print(f'O produto mais barato foi {nomemaisbarato} que custa R${pmaisbarato:.2f}')

