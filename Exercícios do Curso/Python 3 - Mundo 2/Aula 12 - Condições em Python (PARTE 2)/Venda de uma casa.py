casa = float(input('Qual o valor da casa? R$:'))
salario = float(input('Qual o sálario do comprador: R$:'))
anos = int(input('Em quantos anos ele vai pagar?'))
prestacao = (casa / (anos * 12))
minimo = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos '.format(casa, anos))
print('a prestação será de R${:.2f}'.format(prestacao))
if prestacao >= minimo:
    print('Empréstimo NEGADO')
else:
    print('Empréstimo pode ser CONCEDIDO.')
