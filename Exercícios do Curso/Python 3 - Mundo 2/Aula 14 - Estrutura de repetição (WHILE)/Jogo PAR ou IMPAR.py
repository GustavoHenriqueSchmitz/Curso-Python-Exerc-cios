from random import randint #Importando o modulo.
cont = 0 #Contador
print('-' * 25)
print('    Jogo PAR ou ÍMPAR')
print('-' * 25)
while True: #Inicio da repetição e jogo
    c = randint(0, 10) #Faz o computador escolher um número aleatório de 1 a 10
    j = int(input('Digite um número de 0 a 10: ')) #Lugar para o usuario digitar o número que quiser.
    while j > 10 or j < 0: #Repetição para caso o usuario digite um valor fora de 0 a 10
        j = int(input('Apenas números de 0 a 10 serão aceitos, por favor digite novamente: '))
    print('-' * 25)
    j2 = str(input('PAR [P] ou IMPAR [I]: ')).upper().strip() #usuario escolhe seu lado
    while j2 != 'P' and j2 != 'PAR' and j2 != 'I' and j2 != 'IMPAR': #Repetição para caso o usuario escolha um lado que não exista
        j2 = str(input('Apenas digitos PAR [P] ou IMPAR [I] são aceitos: ')).upper().strip()
    s = j + c #Soma do número escolhido pelo computador e número do usuario c e j
    d = s % 2 #Divisão da soma dos números c e j.
    if j2 == 'I' and d != 0: # Se usuario escolher impar e o número for diferente de 0 (NA DIVISÃO) ele vence
        print('-' * 35)
        print(f'Você jogou {j} e o computador {c}. O total foi de {s} e deu IMPAR...')
        print('Jogador venceu')
        print('-' * 35)
    elif j2 == 'P' and d == 0: # Caso o usuario escolher par o número tera que ser 0  (NA DIVISÃO) ele vence
        print('-' * 35)
        print(f'Você jogou {j} e o computador {c}. O total foi de {s} e deu PAR...')
        print('Jogador venceu')
        print('-' * 35)
    else: # Caso contrario o computador vence
        if d == 0:
            print('-' * 35)
            print(f'Você jogou {j} e o computador {c}. O total foi de {s} e deu PAR...')
            print('Computador venceu')
        else:
            print('-' * 35)
            print(f'Você jogou {j} e o computador {c}. O total foi de {s} e deu IMPAR...')
            print('Computador venceu')
        break
    cont += 1 #Contador para contar as vezes que tudo se repetiu ou seja as vezes que o jogador venceu
print('')
print(f'Você venceu {cont} vezes') #Diz quantas vezes o jogador venceu
if cont > 3:
    print('parabéns!')
