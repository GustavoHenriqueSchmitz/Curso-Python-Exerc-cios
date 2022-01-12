v = int(input('Distancia da viagem: '))
print('Você esta preste a começar uma viagem de {}Km'.format(v))
vc = v * 0.50
vl = v * 0.45
if v >200:
    print('A viagem vai custar R${:.2f}'.format(vl))
else:
    print('A viagem vai custar R${:.2f}'.format(vc))
