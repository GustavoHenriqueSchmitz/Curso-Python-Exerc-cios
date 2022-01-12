n1 = [] #Lista
while True: #Repetição
    n = (int(input('Digite um número: ')))
    if n not in n1: #O número só vai ser adicionado se não estiver na lista
        n1.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('O número ja foi digitado, não vou adiciona-lo.')
    continuar = str(input('Quer continuar? [S/N]: ')).upper().strip() #Pergunta se o usuario quer digitar mais números
    while continuar != 'N' and continuar != 'S': #caso o usuario digitar algo errado o programa não prossegue. ou é (S) ou (N)
        continuar = str(input('[S/N]: ')).upper().strip()
    print('')
    if continuar == 'N': #Caso o usuario digitar (N) decidindo que não quer continuar ele quebra a repetição
        break
print('=' *40)
n1.sort() #Organiza a lista em ordem crescente
print(f'Você digitou os valores {n1}') #Escreve a lista
