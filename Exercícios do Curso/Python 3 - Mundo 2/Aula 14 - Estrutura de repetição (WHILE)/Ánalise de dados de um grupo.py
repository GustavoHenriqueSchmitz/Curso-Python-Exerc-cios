cont = cont2 = cont3 = cont4 = 0 #Contadores
while True: #Inicio da repetição
    cont += 1 #Conta as pessoas cadastradas
    print('-' * 25)
    print('   CADASTRE UMA PESSOA')
    print('-' * 25)
    idade = int(input('Idade da pessoa: '))
    sexo = str(input('Sexo da pessoa [M/F]: ')).upper().strip()
    while sexo != 'M' and sexo != 'F': #Repetição para caso o usuario digite um valor que não seja [M/F]
        print('Apenas valores [M/F] são aceitos..')
        sexo = str(input('Sexo da pessoa [M/F]: ')).upper().strip()
    print('-' * 25)
    if idade >= 18: #Verifica apenas as pessoas com mais de 18 anos
        cont2 += 1 #Contador que conta todas as pessoas que possuem mais de 18 anos
    if sexo == 'M': #Verifica apenas os homens cadastrados
        cont3 += 1 #Contador que conta quantos homens foram cadastrados
    if sexo == 'F' and idade < 20: #Verifica apenas as pessoas com menos de 20 anos
        cont4 += 1 #Contador que conta todas as pessoas que possuem menos de 20 anos
    continuar = str(input('Continuar? [S/N]: ')).upper().strip() #Pergunta se o usuario quer continuar ou não
    while continuar != 'S' and continuar != 'N': #Repetição para caso o usuario digite um valor diferente de S ou N
        print('Digite novamente...')
        continuar = str(input('Continuar? [S/N]: ')).upper().strip()
    if continuar == 'N': #Se continuar receber N a repetição será finalizada
        break
print('-' * 25)
print(f'Dessas {cont} pessoas:') #Mostra os resultados
print('')
print(f'{cont2} pessoas tem mais de 18 anos.')
print(f'{cont3} pessoas são homens.')
print(f'{cont4} mulher tem menos de 20 anos.')
