print('-=' * 20)
print(f'{"ANALISANDO UMA LISTA":^40}')
print('-=' * 20)
pos = 0
l = []
l2 = l
while True:
    l.append(int(input('Digite um número: ')))
    continuar = str(input('Quer continuar [S/N]: ')).upper().strip()
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Quer continuar [S/N]: ')).upper().strip()
    if continuar == 'N':
        break
print('-=' * 50)
print(f'Os números digitados forma {l} sendo um total de {len(l)} números digitados.')
for v in l:
    if v != 5:
        pos += 1
    else:
        break
if 5 in l:
    print(f'O número 5 está na lista, na posição {pos}.')
else:
    print('Não encontrei o número 5 na lista.')
l.sort(reverse=True)
print(f'Em ordem decrescente: {l}')
