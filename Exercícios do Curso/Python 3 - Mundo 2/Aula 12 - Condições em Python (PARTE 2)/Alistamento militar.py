g = int(input('Qual das opções?'))
print('')
print('{} nasceu em {} e tem {} anos em {}'.format(nome, nascimento, id, atual))
print('')
if id > 18 and g == 1:
    print('Aliste-se URGENTEMENTE,'
          'Você ja deveria ter se alistado a {} anos.'.format(id - 18))
    print('Em {}'.format(atual - (id - 18)))
elif id == 18 and g == 1:
    print('Você tem que se alistar IMEDIATAMENTE')
elif id < 18 and g ==1:
    print('Você ainda não completou 18 anos, '
          'faltam {} anos para o alistamento.'.format(18 - id))
    print('Você vai ter que se alistar em {}'.format(atual - (id - 18)))
elif g:
    print('O valor digitado é invalido, digite 1 para masculino ou 2 para feminino para prosseguir.')
else:
    print('Você não precissa fazer o alistamento obrigatorio.')
