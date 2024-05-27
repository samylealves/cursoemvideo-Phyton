print('--'*13)
print('   CADASTRE UMA PESSOA')
print('--'*13)
totalmais18 = 0
masculino = 0
mulhermenos20 = 0
while True:
    id = int(input('Idade:'))
    sexo = ''
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
    print('--'*13)
    escolha = ''
    while escolha not in 'SN':
        escolha = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    print('--'*13)
    if id >= 18:
        totalmais18 = totalmais18 + 1
    if sexo == 'Mm':
        masculino = masculino + 1
    if sexo == 'Ff' and id < 20:
        mulhermenos20 = mulhermenos20 + 1
    if escolha == 'N':
        break
print(f'Total de pessoas com mais de 18: {totalmais18} pessoas')
print(f'Ao todo temos {masculino} homens cadastrados')
print(f'E temos {mulhermenos20} mulheres com menos de 20 anos')


