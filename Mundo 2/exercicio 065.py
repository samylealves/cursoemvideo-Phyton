resp = 'S'
soma = quantidade = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número:'))
    soma = soma + num
    quantidade = quantidade + 1
    if num == 1:
        menor = maior = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
media = quantidade/soma
print(f'O total de números digitados foi {quantidade} e sua média é de {media:.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor}')