frase = str(input('Digite uma frase: ')).replace(" ","").upper()
inverso = frase[::-1]
total = ''.join(inverso)
print('A frase {} é {}.'.format(frase, total))
print('')
if frase == total:
    print('A frase É UM PALINDROMO.')
else:
    print('A frase NÃO É UM PALINDROMO.')
