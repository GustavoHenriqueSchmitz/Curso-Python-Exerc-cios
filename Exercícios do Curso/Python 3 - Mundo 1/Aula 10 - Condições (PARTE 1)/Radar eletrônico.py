v = int(input('Velocidade KM:'))
if v > 80:
    print('Multado')
    multa = float(v - 80) * 7
    print('Você ultrapassou o limite de velocidade de 80Km, você deve pagar uma multa de: R$ {:.2f}'.format(multa))
print('')
print('Dirija com segurança.')
