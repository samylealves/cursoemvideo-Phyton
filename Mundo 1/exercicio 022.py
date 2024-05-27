nome = str(input('Digite seu nome completo:')).strip()
print('Analisando o seu nome...')
print('Seu nome em maiúsculo fica {}'.format(nome.upper()))
print('Seu nome em minisculo fica {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)'-'nome.count('')))
d = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(d[0],len(d[0])))
#print('Seu primeiro nome tem {} letras'.format(nome.find('')))

