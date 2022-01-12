nome = str(input('Digite o nome do aluno: '))
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
n = n1+n2
nn = (n+n3) / 3
print('A média do aluno {} foi: {:.1f}'.format(nome, nn))
print('Aprovado'if nn >=7else'Reprovado')
