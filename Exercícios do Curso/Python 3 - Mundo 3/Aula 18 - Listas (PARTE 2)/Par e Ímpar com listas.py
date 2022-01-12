num = [[], []] #Listas a lista par e impar dentro da lista num
for v in range(1, 8): #Repetição para o programa pedir 7 números
    n = int(input(f'Digite o {v}º valor: '))
    if n % 2 == 0: #Verifica se é Par ou ímpar
        num[0].append(n)
    else:
        num[1].append(n)
num[0].sort()#Organiza em ordem crescente
num[1].sort()
print('-=' *20)
print(f'Os valores pares digitados foram: {num[0]}')#Escreve os valores pares
print(f'Os valores impares digitados foram: {num[1]}')#Escreve os valores ímpares
