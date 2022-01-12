nome = str(input('Qual o seu nome completo?')).strip()
x = nome.split()
print('Seu primeiro nome é: {}'.format(x[0]))
print('A Seu segundo nome é: {}'.format(x[len(x)-1]))
