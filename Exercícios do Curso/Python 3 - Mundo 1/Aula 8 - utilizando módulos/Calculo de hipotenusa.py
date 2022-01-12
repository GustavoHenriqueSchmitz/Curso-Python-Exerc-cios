import math
ca1 = float(input('Comprimento do cateto oposto'))
ca2 = float(input('Comprimento do cateto adjacente'))
A = (ca1 ** 2) + (ca2 ** 2)
hipo = math.sqrt(A)
print('A hipotenusa é {:.2f}'.format(hipo))
