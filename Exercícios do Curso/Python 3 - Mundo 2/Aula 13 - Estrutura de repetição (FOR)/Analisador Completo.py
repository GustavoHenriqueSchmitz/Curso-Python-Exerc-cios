somaidade = 0
médiaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1,5):
    print('-----{}ªpessoa-----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        velho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
               totmulher20 += 1
médiaidade = somaidade / 4
print('A média do grupo é {}.'.format(médiaidade))
print('')
print('O homem mais velho possui {} anos e se chama {}.'.format(maioridadehomem, nomevelho))
print('')
print('{} Mulher(es) tem menos de 20 anos.'.format(totmulher20))
