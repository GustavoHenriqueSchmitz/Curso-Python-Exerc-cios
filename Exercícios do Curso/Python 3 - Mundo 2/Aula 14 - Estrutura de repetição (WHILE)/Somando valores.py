print('----------------------------')
print('      SOMANDO VALORES')
print('----------------------------')
n = int(input('Digite um número[Digite 999 para parar]:'))
print('')
cont = 0
soma = 0
n1 = n
while n != 999:
    n = int(input('Digite um número[Digite 999 para parar]:'))
    cont = cont + 1
    if n != 999:
       soma = soma + n
    print('')
print('Você digitou {} números'.format(cont))
print('e a soma entre eles foi {}.'.format(soma + n1))
