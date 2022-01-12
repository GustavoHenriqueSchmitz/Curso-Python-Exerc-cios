soma = cont = 0
while True:
    n = int(input('Digite um número [999 para parar]: '))
    if n == 999:
        break
    soma += n
    cont += 1
    print('')
print(f'A soma de todos os {cont} números digitados é {soma}!')
