print('-=' * 30)
l1 = [] #lista com os números digitados
l2 = []#Lista dos números Pares
l3 = []#Lista dos números ímpares
while True:
    n = int(input('Digite um número: '))
    l1.append(n)
    if n % 2 == 0:
        l2.append(n)
    else:
        l3.append(n)
    continuar = str(input('Quer continuar [S/N]: ')).upper().strip()
    while continuar != 'N' and continuar != 'S':
        continuar = str(input('Quer continuar [S/N]: ')).upper().strip()
    if continuar == 'N':
        break
print('-=' * 21)
print(f'Números digitados: {l1}')
print(f'Números digitados (PARES): {l2}')
print(f'Números digitados (INPARES): {l3}')
