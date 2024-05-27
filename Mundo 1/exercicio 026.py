nome = str(input('Digite sua frase:')).strip()
print('A letra A aparece {} na frase'.format(nome.upper().count('A')))
print('A primeira letra da frase A aparece na posição {}'.format(nome.find('A')+1))
print('A última letra A da frase aparece na posição {}'.format(nome.rfind('A')+1))
