soma = 0
cont = 0
for c in range(1,7):
    n = int(input('Digite o {}ª valor: '.format(c)))
    if n % 2 == 0:
      soma = soma + n
      cont = cont + 1
print('A soma de todos os {} números PARES é: {}'.format(cont, soma))
