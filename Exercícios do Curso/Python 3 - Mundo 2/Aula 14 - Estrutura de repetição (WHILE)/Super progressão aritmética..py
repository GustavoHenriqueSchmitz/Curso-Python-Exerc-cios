primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
termos = 10
while termos != 0:
    decimo = primeiro + (termos - 1) * razao
    i = primeiro
    while i <= decimo:
        print(i, end=" -> ")
        i += razao
    print("...")
    primeiro = i
    termos = int(input("Quantos termos mais? "))
