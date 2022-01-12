from random import randint
from operator import itemgetter
from time import sleep
resultado = {}
for dados in range(1, 5):
    dado = randint(1, 6)
    resultado[f"jogador{dados}"] = dado
print('VALORES SORTEADOS')
for v in range(0, len(resultado)):
    sleep(1)
    print(f'Jogador{v + 1}: {resultado[f"jogador{v + 1}"]}')
print('-=-' * 15)
print(f'{"===RANKING DOS JOGADORES===":^40}')
sleep(2)
resultado = sorted(resultado.items(), key=itemgetter(1))
for c, d in enumerate(resultado[len(resultado):: -1]):
    sleep(1)
    print(f'{f"{c + 1}º lugar: {d[0]} com {d[1]}.":^40}')
