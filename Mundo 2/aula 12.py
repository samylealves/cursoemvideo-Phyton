nome = str(input('Qual é o seu nome? ').upper()).strip()
if nome == 'SAMYLE':
    print('Seu nome é bem excêntrico!')
elif nome == 'MARIA' or nome == 'EDUARDA':
    print('Olá Esposa ;)')
elif nome in 'ANA PAULA JUANA':
    print('nome legal')
else:
    print('Seu nome é bem normal ;)')
print('Tenha um bom dia, {}.'.format(nome.capitalize()))
