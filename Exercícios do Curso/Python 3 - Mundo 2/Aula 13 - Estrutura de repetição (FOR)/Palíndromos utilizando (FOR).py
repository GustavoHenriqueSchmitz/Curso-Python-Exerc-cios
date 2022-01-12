frase = str(input('Digite uma frase: ')).replace(" ","").upper()
palavras = frase.split()
junta = ''.join(palavras)
inverso = ''
for letra in range(len(junta)-1,-1, -1):
    inverso = inverso + junta[letra]
print('A frase {} é {}'.format(frase, inverso),end='')
print('')
if frase == inverso:
    print('\nA frase É UM PALINDROMO.')
else:
    print('\nA frase NÃO É UM PALINDROMO.')
