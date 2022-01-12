e = ('ZERO', 'UM', 'DOIS', 'TRÊS', 'QUATRO', 'CINCO',    #Tupla
     'SEIS', 'SETE', 'OITO', 'NOVE', 'DEZ', 'ONZE',
     'DOZE', 'TREZE', 'CATORZE', 'QUINZE', 'DESSESEIS', 'DESSESETE','DESSOITO', 'DESSENOVE', 'VINTE')
n = int(input('Digite um número de 0 a 20: '))
while n < 0 or n > 20: #Não deixa o usuario avançar se le digitar um valor fora de 0 a 20
    n = int(input('Digite um número de 0 a 20: '))
print(f'Voce digitou > {e[n]} <') #Diz o número digitado por extenso
print('')
continuar = str(input('Quer continuar [S/N]: ')).upper().strip()#Pergunta se o usuario quer continuar
while continuar != 'S' and continuar != 'N': #Não permite o usuario avançar se digitar um valor que não seja N ou S
    continuar = str(input('Quer continuar [S/N]: ')).upper().strip()
print('')
while continuar == 'S': #Enquanto o usuario digitar na variavel (continuar) (S)
    n = int(input('Digite um número de 0 a 20: '))#Ele repete o programa até o usuario decidir que não quer continuar
    while n < 0 or n > 20:
        n = int(input('Digite um número de 0 a 20: '))
    print(f'Voce digitou > {e[n]} <')
    print('')
    continuar = str(input('Quer continuar [S/N]: ')).upper().strip()
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Quer continuar [S/N]: ')).upper().strip()
    print('')
    if continuar == 'N': #Se o usuario Digitar (N) na variavel (continuar) a repetição acaba e o programa termina
        break
print('')
print('Fim do programa')
