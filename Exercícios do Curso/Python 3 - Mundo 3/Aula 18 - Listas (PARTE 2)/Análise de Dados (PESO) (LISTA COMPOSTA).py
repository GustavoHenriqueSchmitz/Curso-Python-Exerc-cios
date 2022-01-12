temp = [] #Lista temporaria
princ = []#Lista principal
cont = menor = maior = 0 #Valores
while True:
    temp.append(str(input('Qual o nome: ')))#Adiciona a lista temporaria o nome digitado
    temp.append(float(input('Qual o peso: ')))#Adiciona a lista temporaria o peso digitado
    if len(princ) == 0: #caso só tenha 1 lista dentro da (princ)
        maior = menor = temp[1] #Ele adiciona essa lista (No caso apenas o peso)ao maior e menor
    else:
        if temp[1] > maior: #caso contrario ele verifica se o número (Peso) da lista temporaria é maior ou menor (Que os valores que estão nas variaveis maior e menor)
            maior = temp[1]#Se o peso da lista temporaria for maior que o armazenado na variavel maior, ele troca pelo peso da temporaria.
        if temp[1] < menor:
            menor = temp[1]# e vise-versa
    princ.append(temp[:])#Após todas as verificações a lista princ recebe uma cópia da lista temporaria.
    temp.clear()#E após isso a lista temporaria é zerada
    continuar = str(input('Quer continuar? [S/N]: ')).strip().upper() #E ele verifica se o usuario quer continuar
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if continuar == 'N': #Se o usuario digitar N a repetição acaba, terminando o programa
        break
print(f'Foram cadastradas {len(princ)} pessoas.')#Mostrando quantas pessoas foram cadastradas
print(f'O peso maior foi {maior}Kg de: ',end=' ') #Qual o peso maior e quais pessoas possuem esse peso
for p in princ:
    if p[1] == maior:
        print(f'{p[0]}', end=' ')
print(f'\nO peso menor foi {menor}Kg de: ', end=' ')##E qual o peso maior e quais pessoas posssuem esse peso
for p in princ:
    if p[1] == menor:
        print(f'{p[0]}', end=' ')
