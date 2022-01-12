import datetime
atual = datetime.date.today().year
cont1 = 0
cont2 = 0
for idade in range(0, 7):
    nasc = int(input('Data de nascimento da {} pessoa.'.format(idade +1)))
    idade2 = atual - nasc
    if idade2 >= 21:
        cont1 = cont1 + 1
    else:
        cont2 = cont2 + 1
print('No total são {} maiores de idade.'.format(cont1))
print('No total são {} menores de idade.'.format(cont2))
