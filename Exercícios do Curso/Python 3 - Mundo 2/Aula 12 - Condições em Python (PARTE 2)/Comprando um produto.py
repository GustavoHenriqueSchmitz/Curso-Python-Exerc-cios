print('{:=^40}'.format(' LOJAS REDY '))
p = float(input('Valor dos produto(s): R$'))
print('Escolha um número abaixo para escolher a forma de pagamento:')
print('')
print('[1] Á vista dinheiro/cheque')
print('')
print('[2] A vista no cartão.')
print('')
print('[3] 2x no cartão.')
print('')
print('[4] 3x ou mais no cartão.')
print('')
op = int(input('Qual das opções?'))
print('')
if op == 1:
    c1 = p - (p * 10 / 100)
    print('Sua compra de R${:.2f} agora vai custar R${:.2f}.'.format(p, c1))
elif op == 2:
    c2 = p - (p * 5 / 100)
    print('Sua compra de R${:.2f} agora vai custar R${:.2f}.'.format(p, c2))
elif op == 3:
    total = p
    parcela = p / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS.'.format(parcela))
    print('Sua compra de R${:.2f} Vai custar R${:.2f} no final.'.format(p, total))
elif op == 4:
    total = p + (p * 20 / 100)
    par = float(input('Quantas parcelas?'))
    c3 = total / par
    print('Sua compra séra parcelada em {:.0f}x de R${:.2f} COM JUROS.'.format(par, c3))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(p, total))
else:
    print('\033[31mOPÇÃO INVALIDA DE PAGAMENTO. >>>TENTE NOVAMENTE<<<')
    print('Sua compra de {:.2f} vai custar {:.2f} no final'.format(p, p))





