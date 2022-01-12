print('=' * 45)
print(f'{"LISTA ORDENADA SEM REPETIÇÕES":^45}') #Basicamente o comando sort
print('=' * 45)
l = list() #lista
for c in range(0, 5): #Repete 5 vezes para o usuario digitar um número
    n = int(input('Digite um numero: '))#Onde o suario digita o número
    if c == 0 or n > l[-1]: #Se o contador for 0 ou seja o algarismo da lista escolhido for o 1 ou se o número digitado (n) for maior que o ultimo número da lista.
        l.append(n) #Ele simplesmente adiciona o número
    else: #Senão ele verifica em qual posição o número está.
        pos = 0 #Posição
        while pos < len(l):
            if n <= l[pos]:
                l.insert(pos, n)
                break
            pos += 1
print('=' * 45)
print(f'{f"Os valores digitados em ordem foram {l}":^45}')
