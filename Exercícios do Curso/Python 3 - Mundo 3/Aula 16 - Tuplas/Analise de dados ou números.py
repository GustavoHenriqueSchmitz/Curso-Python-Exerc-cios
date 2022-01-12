print('-=' * 15)
print('      Analise de dados')
print('-=' * 15)
n = int(input('Digite um número: ')) #Variaveis onde o usuario digita os números.
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite mais um número: '))
n5 = int(input('Digite o ultimo número número: '))
print('')
cont = cont2 = p = 0 #Contadores, e posição.
valores = n, n2, n3, n4, n5 #Tupla com os valores digitados pelo usuario.
print(f'Você digitou os valores: {valores}')
for v in valores: #Repetição.
    if v == 9: #Se o número (v) pego da tupla (valores) for igual a nove.
        cont += 1 #O contador soma 1.
print('-=' * 20)
print(f'O valor 9 foi digitado {cont} vezes.')#Diz quantas vezes o valor 9 foi digitado.
print('-=' * 20)
print('Os números: ',end='') #Parte da repetição abaixo, só não esta dentro da repetição por que iria repetir o print.
for v2 in valores: #Repetição pare vericar os números pares.
    if v2 % 2 == 0:#Parte da repetição onde o número (c) retirado da variavel (valores), é verificado se é par ou não.
        print(f' {v2}, ', end='') #Escreve os números pares, essa print junta com a print de cima.
    if n % 2 != 0 and n2 % 2 != 0 and n3 % 2 != 0 and n4 % 2 != 0 and n5 % 2 != 0:
        print('(Nenhum dos números digitados)',end='')
        break
print(' >>> são pares.')#Complemento das 2 prints acima.
print('-=' * 20)
for v3 in valores: #Repetição para vericar onde o número 3 foi digitado.
    cont2 = cont2 + 1 #Contador que conta a posição onde o número 3 foi digitado.
    if v3 == 3:#Verifica se a variavel (v3) possui o número 3 digitado.
        print(f'O número 3 foi digitado pela primeira ou unica vez, na posição {cont2}.')#Diz onde o número 3 foi digitado.
        print('-=' * 20)
        break #E quebra a repetição.
if n != 3 and n2 != 3 and n3 != 3 and n4 != 3 and n5 != 3:#Porém se nenhuma variavel tiver o número 3 digitado.
    print('O número 3 não foi digitado em nenhuma posição.')
    print('-=' * 20)
print('FIM DO PROGRAMA') #Só para dizer que o programa acabou.
