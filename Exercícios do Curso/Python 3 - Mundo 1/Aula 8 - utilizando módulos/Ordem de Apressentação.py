import random
a1 = str(input('Primeiro aluno:'))
a2 = str(input('Segundo aluno:'))
a3 = str(input('terceiro aluno:'))
a4 = str(input('quarto aluno:'))
L = [a1, a2, a3, a4]
E = random.shuffle(L)
print('A ordem é: {}'.format(L))
#print('A ordem de trabalho será.')
#print('{}'.format(L))
