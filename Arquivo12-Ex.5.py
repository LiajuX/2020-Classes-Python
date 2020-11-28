valorI = int(input("Informe o valor inicial\n"))
valorF = int(input("Informe o valor final\n"))

for valor in range (valorI,valorF + 1,1):
    quadrado = valor * valor
    print(quadrado)
