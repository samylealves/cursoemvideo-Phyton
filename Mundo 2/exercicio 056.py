somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for c in range(1, 5):
    print('---- {}° PESSOA ----'.format(c))
    nome = str(input('Nome:')).strip().capitalize()
    id = int(input('Idade:'))
    sexo = str(input('Sexo [M/F]:')).strip()
    somaidade = somaidade + id
    if c == 1 and sexo in 'Mm':
        maioridadehomem = id
        nomevelho = nome
    if sexo in 'Mm' and id > maioridadehomem:
        maioridadehomem = id
        nomevelho = nome
    if sexo in 'Ff' and id > 20:
        totmulher20 = totmulher20 + 1

mediaidade = somaidade / 4
print('A média de idade do grupo é de {}'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))




