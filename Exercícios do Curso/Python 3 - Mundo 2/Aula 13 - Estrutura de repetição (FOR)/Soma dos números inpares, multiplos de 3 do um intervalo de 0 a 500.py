soma = 0
cont = 0
for inter in range(0, 501):
    c1 = inter % 3
    c2 = inter % 2
    if c1 == 0 and c2 == 1:
        cont = cont + 1
        soma = soma + inter
print('A soma de todos os {} valores solicitados é: {}'.format(cont,soma))
