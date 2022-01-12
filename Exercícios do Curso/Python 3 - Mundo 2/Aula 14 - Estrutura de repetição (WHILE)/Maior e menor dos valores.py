cont = media = soma = maior = menor = 0
continuar = str(input('''Digite quantos números quiser para calcular a média e verificar qual o menor e maior dos números.
Digite [S] quando quiser começar:''').strip().upper())
while continuar != 'S':
    print('')
    print('!!!Valor digitado invalido!!!')
    continuar = str(input('Digite [S] quando quiser começar: ')).strip().upper()
print('')
while continuar == 'S':
    n = int(input('Digite um número: '))
    continuar = str(input('Quer continuar[S/N]: ')).upper().strip()
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Digite[S/N] para prosseguir: ')).upper().strip()
    cont = cont + 1
    soma = soma + n
    if cont == 1:
        maior = n
        menor = n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    media = soma / cont
    print('')
print('A média de todos os {} números digitados é {}.'.format(cont, media))
print('O menor valor foi {} e o maior foi {}.'.format(menor, maior))
