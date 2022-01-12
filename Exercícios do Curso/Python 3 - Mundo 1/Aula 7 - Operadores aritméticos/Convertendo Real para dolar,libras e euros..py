real = float(input('Quanto dinheiro você tem na carteira? R$'))
Dolar = real/5.11
Euro = real/6.19
Libra = real/6.83
print('Com R${} você pode comprar {:.2f}US$(Dolar)'.format(real,Dolar))
print('Com R${} você pode comprar {:.2f}¢(Euros)'.format(real,Euro))
print('Com R${} você pode comprar {:.2f}£(Libras)'.format(real,Libra))
