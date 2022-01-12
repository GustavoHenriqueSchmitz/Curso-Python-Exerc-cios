import random
import time
print('-=-' * 17)
print('VOU ESCOLHER UM NÚMERO DE 0 A 5, TENTE ADIVINHAR')#Faz o computador "Pensar"
print('-=-' * 17)
computador= (random.randint(0, 5))
jogador = int(input('Em que número pensei: ')) #Jogador tenta adivinhar
print('Processando...')
time.sleep(1.5)
if computador==jogador:
    print('Parabéns você me venceu')
else:
    print('GANHEI, eu pensei no número {} e não no número {}'.format(computador, jogador))
