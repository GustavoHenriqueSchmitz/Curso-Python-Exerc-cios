import random
A = str(input('Primeiro aluno'))
B = str(input('Segundo Aluno'))
C = str(input('Terceiro aluno'))
D = str(input('Quarto aluno'))
L = [A, B, C, D]
E = random.choice(L)
print('O aluno escolhido é {}'.format(E))
