import time
v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
print('     [1] Somar')
print('     [2] Multiplicar')
print('     [3] Maior')
print('     [4] Novos números')
print('     [5] Sair do programa')
op = int(input('>>>>> Qual é a sua opção: '))
time.sleep(0.2)
while op != 1 and op != 2 and op != 3 and op != 4 and op != 5:
    print('!!!! Valor digitado invalido !!!!')
    op = int(input('>>>>> Qual é a sua opção: '))
    time.sleep(0.2)
while op != 5:
    if op == 1:
        print('A soma entre {} e {} é: {} '.format(v1, v2, v1 + v2))
        print('=' * 22)
    if op == 2:
        print('A multiplicação entre {} e {} é: {}'.format(v1, v2, v1 * v2))
        print('=' * 22)
    if op == 3:
        if v1 > v2:
            print('O número maior é: {}.'.format(v1))
            print('=' * 22)
        elif v1 == v2:
            print('Os números são iguais.')
            print('=' * 22)
        else:
            print('O número maior é: {}.'.format(v2))
            print('=' * 22)
    if op == 4:
        print('Informe os valores novamente.')
        v1 = int(input('Primeiro valor: '))
        v2 = int(input('Segundo valor: '))
    print('     [1] Somar')
    print('     [2] Multiplicar')
    print('     [3] Maior')
    print('     [4] Novos números')
    print('     [5] Sair do programa')
    op = int(input('>>>>> Qual é a sua opção: '))
    print('=' * 22)
    while op != 1 and op != 2 and op != 3 and op != 4 and op != 5:
        print('!!!! Valor digitado invalido !!!!')
        op = int(input('>>>>> Qual é a sua opção: '))
        time.sleep(0.2)
    time.sleep(0.2)
if op == 5:
    print('')
    print('Finalizando...')
    print('=' * 22)
    time.sleep(1)
    print('Fim do programa, volte sempre.')
