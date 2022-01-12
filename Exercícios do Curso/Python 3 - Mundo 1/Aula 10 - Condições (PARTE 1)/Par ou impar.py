n = int(input('Digite qualquer número: '))
pi = n % 2
if pi == 0:
    print('O número {} é par'.format(n, pi))
else:
    print('O número {} é impar'.format(n))
