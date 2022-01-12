from datetime import date
at = date.today().year
nasc = int(input('Qual ano o atleta nasceu?'))
id = at - nasc
print('')
print('O atleta tem {} anos.'.format(id))
print('')
if id > 0 and id <= 9:
    print('Classificação: MIRIM')
elif id > 9 and id <= 14:
    print('Classificação: INFANTIL')
elif id > 14 and id <=19:
    print('Classificação: JÚNIOR')
elif id > 19 and id <=25:
    print('Classificação: SÊNIOR')
elif id > 25:
    print('Classificação: MASTER')
