while True:
    num = int(input('Digite o número que deseja ver a tabuada:'))
    print('--'*15)
    if num < 0:
        break
    for c in range(1, 11):
        print(f'{num} x {c} = {num*c}')
    print('--'*15)
print('PROGRAMA DE TABUADA ENCERRADO. Volte sempre!')

