import random
import time
l1 = ('Papel', 'Pedra', 'Tesoura')
computador =random.randint(0, 2)
print('{:=^45}'.format('JOGO: PEDRA, PAPEL, TESOURA.'))
print('Escolha uma das opções:')
print('')
print('\033[33m[0] papel')
print('')
print('[1] pedra')
print('')
print('[2] Tesoura\033[m')
print('')
j = int(input('Qual a sua jogada: '))
print('JO')
time.sleep(0.6)
print('KEN')
time.sleep(0.6)
print('PO')
time.sleep(0.4)
print('-='*11)
print('Computador jogou: {}'.format(l1[computador]))
print('Jogador jogou: {}'.format(l1[j]))
print('-='*11)
if computador == 0: # computador jogou PAPEL
    if j == 0:
        print('EMPATE') #Jogador jogou PAPEL
    elif j == 1:
        print('Computador VENCEU')#Jogador jogou PEDRA
    elif j == 2:
        print('Jogador VENCEU')#Jogador jogou TESOURA
    else:
        print('Jogada invalida.')
elif computador == 1: # computador jogou PEDRA
        if j == 0:
            print('Jogador VENCEU') #Jogador jogou PAPEL
        elif j == 1:
            print('EMPATE') #Jogador jogou PEDRA
        elif j == 2:
            print('Computador VENCEU')#Jogador jogou TESOURA
        else:
            print('Jogada invalida.')
elif computador == 2: #Computador jogou TESOURA
            if j == 0:
                print('Jogador PERDEU') #Jogador jogou PAPEL
            elif j == 1:
                print('Jogador VENCEU') #Jogador jogou PEDRA
            elif j == 2:
                print('EMPATE') #Jogador jogou TESOURA
            else:
                print('Jogada invalida.')
