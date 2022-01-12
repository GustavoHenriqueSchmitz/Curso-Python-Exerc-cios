n = int(input('Digite um número para\ncalcular seu fatorial'))
f = 1
for n in range(n, 0, -1):
    print(' {}'.format(n),end= '')
    print(' x' if n > 1 else ' = ',end= '')
    f = f * n
print(f,end='')
