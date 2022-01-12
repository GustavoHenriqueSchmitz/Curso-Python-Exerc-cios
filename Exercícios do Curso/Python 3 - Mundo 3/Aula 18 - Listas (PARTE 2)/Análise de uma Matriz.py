matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] #Lista (Com as três listas da matriz)
somapares = soma = cont = maior = 0 #variaveis
segundacoluna = []
for c in range(0, 3): #colunas
    for l in range(0, 3): #linhas
        matriz[c][l] = int(input(f'Digite um valor para [{c}, {l}]: ')) #pede um valor
print('-=' *25)
for l in matriz: #escreve a matriz
    for v in range(0, 3):
        print(f'[{l[v]:^5}]',end='')
    print('')
for l in matriz: #Após escrever a matriz, ele verifica lista por lista dentro da lista (MATRIZ)
    for v in range(0, 3): #verifica se o número é par
        if l[v] % 2 == 0:
            somapares += l[v]
        if v == 2: #Soma os valores da terceira coluna
            soma += l[v]
        if v == 1: #verifica qual o maior valor da segunda coluna
            segundacoluna.append(l[v])
            maior = max(segundacoluna)
print('-=' * 25)
print(f'A soma de todos os números pares da matriz é: {somapares}')#escreve os resultados
print(f'A soma de todos os valores da terecira coluna é: {soma}')
print(f'O maior número da segunda coluna é: {maior}')

