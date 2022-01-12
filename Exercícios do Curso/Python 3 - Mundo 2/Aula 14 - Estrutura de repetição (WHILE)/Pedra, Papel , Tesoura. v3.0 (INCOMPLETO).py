import random
import time
palpite = 0
palpite2 = 0
palpite3 = 0
palpite4 = 0
palpite5 = 0
palpite6 = 0
f = random.randint(1, 10)
m = random.randint(1, 100)
d = random.randint(1, 1000)
f2 = random.randint(1, 10)
m2 = random.randint(1, 100)
d2 = random.randint(1, 1000)
print('')
print('{:=^45}'.format('JOGO DA ADIVINHAÇÃO'))
time.sleep(1)
print('')
print('Ola sou o seu computador vamos jogar o jogo da adivinhação?')
time.sleep(2)
print('primeiro vamos decidir a dificuldade.')
print('')
time.sleep(1.5)
print('[1] Facil')
print('Nessa dificuldade vou escolher um número de 0 a 10.')
time.sleep(2.5)
print('[2] Médio')
print('Nessa  dificuldade vou escolher um número de 0 a 100.')
time.sleep(2.5)
print('[3] Dificil')
print('Nessa dificuldade vou escolher um número de 0 a 1000. (Boa Sorte)')
time.sleep(2.5)
print('')
dificuldade = str(input('Em qual dificuldade você vai querer jogar?')).upper().strip()
print('Definindo dificuldade...')
print('')
time.sleep(2)
if dificuldade == '1':
    print('Pensei em um número de 0 a 10.')
    time.sleep(1.9)
    print('Você consegue adivinhar qual foi?')
    time.sleep(1.5)
    print('')
    j = int(input('Qual o seu palpite?'))
    time.sleep(0.2)
    while j != f:
        if j < f:
            j = int(input('Mais...Tente novamente: '))
        else:
            j = int(input('Menos... Tente novamente: '))
            time.sleep(0.2)
        palpite = palpite + 1
    print('')
    print('Acertou com {} tentativas. Parabéns!'.format(palpite))
if dificuldade == '2':
    print('Pensei em um número de 0 a 100.')
    time.sleep(1.9)
    print('Você consegue adivinhar qual foi?')
    time.sleep(1.5)
    print('')
    j = int(input('Qual o seu palpite?'))
    time.sleep(0.2)
    while j != m:
        if j < m:
            j = int(input('Mais...Tente novamente: '))
        else:
            j = int(input('Menos... Tente novamente: '))
            time.sleep(0.2)
        palpite2 = palpite2 + 1
    print('')
    print('Acertou com {} tentativas. Parabéns!'.format(palpite2))
if dificuldade == '3':
    print('Pensei em um número de 0 a 1000.')
    time.sleep(1.9)
    print('Você consegue adivinahar qual foi?')
    time.sleep(1.5)
    print('')
    j = int(input('Qual o seu palpite?'))
    time.sleep(0.2)
    while j != d:
        if j < d:
            j = int(input('Mais...Tente novamente: '))
        else:
            j = int(input('Menos...Tente novamente'))
            palpite3 = palpite3 + 1
    print('Você acertou com {} tentativas. Parabéns!'.format(palpite3))
continuar = str(input('Quer jogar de novo?[Sim/Não]: ')).strip()[0]
while continuar == 'S' or 's':
    time.sleep(0.5)
    print('')
    print('Escolha a dificuldade:')
    print('[1] Facil')
    time.sleep(1)
    print('[2] Médio')
    time.sleep(1)
    print('[3] Dificil')
    time.sleep(1)
    print('')
    dificuldade2 = int(input('Em qual dificuldade você vai querer jogar?'))
    print('Definindo dificuldade...')
    print('')
    time.sleep(2)
    if dificuldade2 == 1:
        print('Pensei em um número de 0 a 10.')
        time.sleep(1.9)
        print('Você consegue adivinhar qual foi?')
        time.sleep(1.5)
        print('')
        j2 = int(input('Qual o seu palpite?'))
        time.sleep(0.2)
        while j2 != f2:
            if j2 < f2:
                j2 = int(input('Mais...Tente novamente: '))
            else:
                j2 = int(input('Menos... Tente novamente: '))
                time.sleep(0.2)
            palpite4 = palpite4 + 1
    print('')
    print('Acertou com {} tentativas. Parabéns!'.format(palpite4))
    if dificuldade2 == 2:
        print('Pensei em um número de 0 a 100.')
        time.sleep(1.9)
        print('Você consegue adivinhar qual foi?')
        time.sleep(1.5)
        print('')
        j = int(input('Qual o seu palpite?'))
        time.sleep(0.2)
        while j2 != m2:
            if j2 < m2:
                j2 = int(input('Mais...Tente novamente: '))
            else:
                j2 = int(input('Menos... Tente novamente: '))
                time.sleep(0.2)
            palpite5 = palpite5 + 1
        print('')
        print('Acertou com {} tentativas. Parabéns!'.format(palpite2))
    if dificuldade2 == 3:
        print('Pensei em um número de 0 a 1000.')
        time.sleep(1.9)
        print('Você consegue adivinahar qual foi?')
        time.sleep(1.5)
        print('')
        j = int(input('Qual o seu palpite?'))
        time.sleep(0.2)
        while j2 != d2:
            if j2 < d2:
                j2 = int(input('Mais...Tente novamente: '))
            else:
                j2 = int(input('Menos...Tente novamente'))
                palpite6 = palpite6 + 1
        print('Você acertou com {} tentativas. Parabéns!'.format(palpite3))
    continuar = str(input('Quer jogar de novo?[Sim/Não]: ')).upper().strip()[0]
