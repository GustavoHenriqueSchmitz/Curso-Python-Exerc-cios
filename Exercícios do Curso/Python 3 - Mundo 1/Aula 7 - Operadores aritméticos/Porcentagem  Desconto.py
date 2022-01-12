Preço = float(input('Qual é o preço do produto'))
c1 = Preço * 5
c2 = c1 / 100
c3 = Preço - c2
# novo = Preço - (Preço * 5 / 100)
print('O desconto é de 5%, o valor do desconto é R${:.2f}, Sendo o preço agora na promoção R${:.2f}'.format(c2, c3))
