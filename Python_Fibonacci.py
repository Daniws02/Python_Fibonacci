n = int(input("Digite a quantidade de números: "))

anterior = 0
proximo = 1
quantidade = 0

while quantidade < n:
    quantidade = quantidade + 1
    print(proximo)
    proximo = proximo + anterior
    anterior = proximo - anterior
