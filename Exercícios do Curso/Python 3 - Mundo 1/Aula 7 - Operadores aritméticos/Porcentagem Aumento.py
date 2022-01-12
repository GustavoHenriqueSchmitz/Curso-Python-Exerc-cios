nome = input('Nome do funcionário')
salário = float(input('Sálario R$'))
#aumento = salário + (salário*15/100)
aumento = salário * 15 / 100
total = salário + aumento
print(' O funcionario {} teve um aumento de 15% R${:.2f}, seu salário agora passou de R${:.2f} para R${:.2f}.'.format(nome,aumento,salário,total))
