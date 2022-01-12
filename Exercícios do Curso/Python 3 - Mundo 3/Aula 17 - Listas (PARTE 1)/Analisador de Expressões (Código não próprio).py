exp = list()
exp.append(str(input('Digite um expressão: ')))
cont =0
cont2 =0
for i in exp[0]:
    if i =='(':
        cont = cont+1
    elif i == ')':
        cont2 = cont2+1
    if cont2 > cont:
        break
if cont == cont2:
    print('Essa expressão é válida!')
else:
    print('Essa expressão não é válida!')
