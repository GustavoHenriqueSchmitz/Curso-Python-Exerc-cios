import math

an = float(input('Digite o angulo que você deseja:'))
ra = math.radians(an)
co = math.cos(ra)
se = math.sin(ra)
ta = math.tan(ra)
print('O valor do SENO é {:.2f}'.format(se))
print('O valor do COSSENO é {:.2f}'.format(co))
print('O valor do TANGENTE é {:.2f}'.format(ta))
