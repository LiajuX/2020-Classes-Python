N = int(input("Informe a base\n"))
M = int(input("Informe o expoente\n"))

potencia = 1

for i in range (0,M,1):
    potencia *= N

print(N, "elevado a", M, "é igual a", potencia)
