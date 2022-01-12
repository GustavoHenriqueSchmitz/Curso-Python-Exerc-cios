print('Gerador de PA')
print('-=-'* 5)
p1 = int(input('Primeiro termo:'))
p2 = int(input('Razão:'))
termo = p1
cont = 1
while cont <= 10:
    print('{} → '.format(termo), end='')
    termo = termo + p2
    cont = cont + 1
print('FIM')
