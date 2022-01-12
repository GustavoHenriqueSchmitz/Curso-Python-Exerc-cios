import math

ca1 = float(input('Digite o valor do cateto oposto:'))
ca2 = float(input('Digite o valor do cateto adjuncente:'))
hi = math.hypot(ca1, ca2)
print('A hipotenusa é {:.2f}'.format(hi))
