cont = cont2 = soma = barato = 0 #Contadores e somadores
barato2 = ''
print('-' * 25)
print('    LOJA SUBERBARATÃO')
print('-' * 25)
while True:
    nome = str(input('Nome do produto: '))#Usuario digita o nome do produto
    p = float(input('Preço do produto: R$'))#Usuario digita o preço do produto
    print('-' * 25)
    cont += 1 #Contador que conta quantos produtos foram comprados
    soma += p #Soma todos os preços
    if p >= 1000: #Se o preço for maior que 1000
        cont2 += 1 #Contador que conta todos os produtos que custam mais de 1000
    if cont == 1: #Para definir o produto mais barato
        barato = p #Preço do produto mais barato
        barato2 = nome #Nome do produto mais barato
    if p < barato:
        barato = p #Preço do produto mais barato
        barato2 = nome #Nome do produto mais barato
    continuar = str(input('Continuar [S/N]: ')).upper().strip()#Usuario escolhe se quer continuar ou não
    while continuar != 'S' and continuar != 'N': #Caso o usuario digite um valor que não corresponda a [S/N]
        continuar = str(input('Continuar [S/N]: ')).upper().strip()
    if continuar == 'N':#Caso o usuario digite N no campo continuar a repetição será finalizada
        break
print('--------------FIM DO PROGRAMA--------------')
print(f'Dos {cont} produtos comprados:') #Quantia de produtos comprados
print('')
print(f'O valor total de todos os produtos é: R${soma:.2f}') #Valor total de todos os produtos
print(f'{cont2} produto(s) custam mais de R$1000.00.') #Quantos produtos custam mais de 1000
print(f'O produto mais barato foi o(a) {barato2} custando R${barato:.2f}.') #Define qual foi o produto mais barato
