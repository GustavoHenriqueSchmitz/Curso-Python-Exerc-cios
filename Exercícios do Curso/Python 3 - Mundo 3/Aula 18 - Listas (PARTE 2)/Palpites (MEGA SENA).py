from random import randint #Importa o modulo random (randint) e time (sleep)
from time import sleep
print('-' * 40)
print(f'{"JOGA NA MEGA SENA":^40}')
print('-' * 40)
numeros = [] #lista temporaria que guarda os números sorteados
jogos = [] #Lista permanente que guarda todos os números sorteados
cont = 0 #Contador
quant = int(input('Quantos jogos você quer que eu sorteie? '))#Pergunta e guarda na variavel(JOGOS), a quantia de jogos que vão ser sorteados
for j in range(quant): #Aqui o programa começa a sortear a quantia de jogos desejada
    for n in range(1, 7): #Sorteia 6 números de 1 a 60
        sorteio = randint(1, 60)
        while sorteio in numeros: #Mas se o número sorteado ja estiver na lista (numeros), outro número será sorteado
            sorteio = randint(1, 60)
        numeros.append(sorteio)#Após sortear e verificar se o número ja está na lista ele adiciona
        if n == 6: #Se for o 6º sorteio, ele vai adicionar uma cópia da lista numeros a lista jogos e depois zera a lista numeros
           jogos.append(numeros[:])
           numeros.clear()
print('-=-=-= SORTEANDO {jogos} JOGOS -=-=-=')
for s in range(0, quant): #Escreve os jogos
    cont += 1
    sleep(0.5)
    print(f'Jogo {cont}: {jogos[s]}')#Escreve os jogos e seus números sorteados, utilizando o contador para definir qual o jogo
print('-=-=-=-=-= < BOA SORTE > -=-=-=-=-=')
