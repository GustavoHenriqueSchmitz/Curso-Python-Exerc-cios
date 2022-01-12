print('-' * 40)
print(f'{"ANALISADOR DE PALAVRAS":^40}')
print('-' * 40)
palavras = ('aprender', 'programar', 'linguagem', 'python',
           'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro') #Tupla
for v in palavras: #Repetição que pega valor por valor da tupla
    print('')
    print(f'\033[31mNa palavra ({v}). \033[m') #Escreve qual a palavra
    print(f'\033[35mTemos como vogais as letras:\033[m',end='')#Print 1
    for l in v:
        if l == 'a' or l == 'e' or l == 'i' or l == 'o' or l == 'u':
            print(f'\033[34m {l} ',end='') #Junta com a print 1, (Revela as vogais)
