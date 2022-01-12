seg1 = float(input('Primeiro segmento: '))
seg2 = float(input('Segundo segmento: '))
seg3 = float(input('Terceiro segmento: '))
if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg2 + seg1 and seg1 == seg2 == seg3:
    print('Com esses segmentos é POSSIVEL formar um triângulo equilatero.')
elif seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg2 + seg1 and seg1 == seg2 or seg1 == seg3 or seg2 == seg3 or seg2 == seg1 or seg3 == seg1 or seg3 == seg2:
    print('Com esses segmentos é POSIVEL formar um triângulo isósceles.')
elif seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg2 + seg1:
    print('Com esses segmentos é POSSIVEL formar um triângulo escaleno.')
else:
    print('NÃO É POSSIVEL formar um triângulo.')
