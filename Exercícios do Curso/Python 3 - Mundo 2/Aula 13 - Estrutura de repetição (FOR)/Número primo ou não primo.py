tot = 0
n = int(input('Digite um número: '))
for p in range(1, n + 1, +1):
    if n % p == 0:
        tot = tot + 1
        print('\033[34m', end=" ")
    else:
       print('\033[m', end=" ")
    print('{}'.format(p), end=" ")
print('\n \033[m O número {} foi divisivel por {} vezes'.format(n, tot))
if tot == 2:
    print('\n \033[m O número É PRIMO.')
else:
    print('\n \033[m O número NÃO É PRIMO.')
