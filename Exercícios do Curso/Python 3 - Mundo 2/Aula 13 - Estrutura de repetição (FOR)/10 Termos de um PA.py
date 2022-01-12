('='*28)
print('    10 TERMOS DE UMA PA')
print('='*28)
Primeiro = int(input('Primeiro termo: '))
Razao = int(input('Razão: '))
for PA in range(Primeiro, Primeiro + Razao * 10, Razao):
    print(PA, end=' → ')
print('ACABOU')
