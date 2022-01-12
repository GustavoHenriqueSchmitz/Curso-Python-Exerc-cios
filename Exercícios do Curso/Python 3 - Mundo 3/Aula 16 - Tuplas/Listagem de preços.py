cont = cont2 = 0 #Contadores
p = ('Lapís', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99,
     'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)#Tupla
print('-' * 42)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 42)
for pos in range(0, len(p)):
    if pos % 2 == 0:
        print(f'{p[pos]:.<30}',end='') #Diz o produto
    else:
        print(f'R${p[pos]:>8.2f}')#Diz o preço
