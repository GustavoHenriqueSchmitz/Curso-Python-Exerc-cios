dicionario = {}
dicionario['nome'] = str(input('Nome do aluno: '))
dicionario['media'] = float(input(f'Média do aluno {dicionario["nome"]}: '))
print('=-' * 20)
print(f'O nome é {dicionario["nome"]}')

print(f'A média é {dicionario["media"]}')
if dicionario['media'] >= 7:
    print('Situação: Aluno APROVADO')
elif dicionario['media'] >= 5 and dicionario['media'] < 7:
    print('Situação: Aluno em RECUPERAÇÂO')
else:
    print('Situação: Aluno REPROVADO')
