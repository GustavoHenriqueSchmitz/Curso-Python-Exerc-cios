n = int(input('Digite um número para ver a sua tabuada: '))
for tab in range(0, 11, +1):
    print('{} * {:2} = {}'.format(n, tab, n * tab))
