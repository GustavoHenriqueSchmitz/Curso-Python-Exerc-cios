n1 = int(input('Um valor'))
n2 = int(input('Outro valor'))
s = n1+n2
d = n1*n2
g = n1/n2
di = n1//n2
e = n1 ** n2
print('A soma é {}, \n o produto é {} a \n divisão é {:.3f} '.format(s,d,g,), end ='')
print('Divisão inteira {} e Potência {}'.format(di,e))
