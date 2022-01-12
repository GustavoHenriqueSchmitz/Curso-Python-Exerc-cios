nomenota = [] #lista Temporaria com o nome e as notas dos alunos
nomemedia = [] #Lista temporaria com o nome e as médias dos alunos
nomenotaper = [] #lista permanente com o nome e as notas dos alunos
boletim = [] #Lista permanente com o nome dos alunos e suas médias
while True:
    #Código (WHILE) principal que organiza todas as listas, começa perguntando o nome, primeira nota e segunda.
    nome = (str(input('Nome do aluno:')))
    nota1 = (float(input('Nota 1: ')))
    nota2 = (float(input('Nota 2: ')))
    # Após decidir o nome e as notas ele começa a dividir os valores nas listas temporarias primeiro e depois copia os valores
    # na forma de lista adicionando dentro das listas permanentes
    # e após isso reinicia as listas (Temporarias) apagando elas
    # e caso o usuario digite que quer adicionar mais um aluno o código começa tudo de novo.
    nomenota.append(nome)
    nomenota.append(nota1)
    nomenota.append(nota2)
    media = (nota1 + nota2) / 2 #Aqui ele forma a média das notas
    nomemedia.append(nome)
    nomemedia.append(media)
    nomenotaper.append(nomenota[:])
    boletim.append(nomemedia[:])
    nomenota.clear()#Aqui onde ele limpa/reinicia as listas
    nomemedia.clear()
    continuar = str(input('Quer continuar? [S/N]: ')).upper().strip()#Aqui ele verifica se o usuario quer adicionar mais alunos
    while continuar != 'N' and continuar != 'S':
        continuar = str(input('Quer continuar? [S/N]: ')).upper().strip()
    if continuar == 'N':
        break
print('-=' *25)
print(f'{"No.":^2} {"Nome.":^5} {"Média.":^15}')#Aqui ele começa a escrever os resultados
print('-' * 25)
for n, v in enumerate(boletim):
    print(f'{n} {v[0]:^8} {v[1]:^11}') #escrevendo primeiro o nome e a média de cada aluno, cada aluno tem seu número começando por 0
print('-' * 28)
while True:#E após, pergunta se o usuario quer ver a nota de algum aluno individualmente até o usuario digitar 999 e terminar o programa
    notaaluno = int(input('De qual aluno você quer ver a nota? [999 para para]: '))
    while notaaluno >= len(nomenotaper) and notaaluno != 999:
        print('-' * 50)
        notaaluno = int(input('De qual aluno você quer ver a nota? [999 para para]: '))
    if notaaluno == 999:
        break
    print('-' * 50)
    print(f'As notas de {nomenotaper[notaaluno][0]} são {nomenotaper[notaaluno][1:3]}') #Aqui ele escreve o resultado do aluno escolhido
print('-=' * 25)
print('FIM DO PROGRAMA')
