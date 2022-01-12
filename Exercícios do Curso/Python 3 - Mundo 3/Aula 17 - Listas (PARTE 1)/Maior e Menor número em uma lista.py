n = []
cont = cont2 = 0
for c, v in enumerate(range(0, 5)):
    n.append(int(input(f'Digite um valor na posição {c}: ')))
    maior = max(n)
    menor = min(n)
print('=-=' * 17)
print(f'Você digitou os valores {n}')
print(f'O menor número da lista  é {menor} na posição: ',end='')
for v in (n):
    if v == menor:
        print(cont,end='...')
    cont += 1
print(f'\nO maior número da lista é {maior} na posição: ', end='')
for v in (n):
    if v == maior:
        print(cont2, end='...')
    cont2 += 1
