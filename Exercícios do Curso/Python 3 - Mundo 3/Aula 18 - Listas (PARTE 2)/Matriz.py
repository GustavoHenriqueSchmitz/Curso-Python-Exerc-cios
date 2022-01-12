matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] #Lista (Com as três listas da matriz)
for c in range(0, 3): #Define a coluna
    for l in range(0, 3): #Define a linha
        matriz[c][l] = int(input(f'Digite um valor para [{c}, {l}]: ')) #Pede um valor
print('-=' * 20)
for l in matriz: #escreve a matriz
    for v in range(0, 3):
        print(f'[{l[v]:^5}]',end='')
    print('')
