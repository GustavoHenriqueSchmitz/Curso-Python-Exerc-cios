peso = float(input('Qual o seu peso? (Kg) '))
tamanho = float(input('Qual o seu tamanho? (m)'))
imc = peso / (tamanho * tamanho)
if imc < 18.5:
    print('IMC: {:.1f}\nAbaixo do peso'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('IMC: {:.1f}\nPeso ideal'.format(imc))
elif imc >= 25 and imc < 30:
    print('IMC: {:.1f}\nSobrepesso'.format(imc))
elif imc >= 30 and imc < 40:
    print('IMC: {:.1f}\nObesidade')
elif imc >= 40:
    print('IMC {:.1f}\nObesidade mórbida'.format(imc))
