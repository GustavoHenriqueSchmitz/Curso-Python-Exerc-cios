cont = 0 #Contador
times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco da Gama', 'Chapecoense', 'Atlético', 'Botafogo', 'Atlético-PR',
         'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO') #Tupla
print('-=-' *20)
print(f'Listas de time do Brasileirão: {times}') #Mostra todos os times
print('-=-' *20)
print(f'Os 5 primeiros da lista são {times[0: 5]}') #Mostra os 5 primeiros
print('-=-' *20)
print(f'E os ultímos 4 colocados são {times[16:]}')#Mostra os ultimos 4
print('-=-' *20)
print(f'Os times ordenados alfabeticamente são: {sorted(times)}')#Mostra os times em ordem alfabética
print('-=-' *20)
print(f'A chapecoense está na {times.index("Chapecoense")+1}ª posição')#Mostra onde está a chapecoense
