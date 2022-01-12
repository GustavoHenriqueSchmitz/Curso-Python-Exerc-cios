cont = 0 # Contador
t = 0
t = int(input('De qual número você quer ver a tabuada[Digite um número negativo para parar]: ')) #Variavel para o usuario digitar o valor da tabuada
#que ele quer
print('-=-' * 25)
while cont != 11:# Inicio da repetição, para montar a tabuada, ele repete até o contador chegar a 11.
    print('{} x {} = {}'.format(t, cont, t * cont)) # A tabuada será escrita aqui.
    cont += 1# Contador
    if cont == 11:# Quando o contador chegar a 11 ele iria parar a repetição.
        cont -= 11# Para resolver isso basta reiniciar o contador
        print('-=-' * 25)
        t = int(input('De qual número você quer ver a tabuada[Digite um número negativo para parar]: '))
        print('-=-' * 25)
    if t < 0:#Define que os números negativos serão a ferramenta para fechar o programa
        break
print('')
print('Fim do programa. Volte sempre.')
