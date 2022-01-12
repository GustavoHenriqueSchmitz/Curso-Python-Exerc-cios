from random import randint #Importa o modulo randint

numeros = randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10) #Tupla com os números aleatórios de 1 a 10
print(f'Os valores sorteados foram: ', end='') #Diz os valores sorteados
for n in numeros: #Repetição para dizer os número sorteados
    print(f'{n}', end=' ')
print(f'\nO Maior valor foi: {max(numeros)}') #Diz qual o maior valor
print(f'O menor valor foi: {min(numeros)}') #Diz qual o menor valor
