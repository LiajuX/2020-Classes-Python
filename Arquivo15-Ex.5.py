nomes = []

for i in range (5):
    nomes.append(input("Insira o " + str(i+1) + "º nome: "))

print("\nLista de nomes:")

for i in range(5):
    print(str(i+1) + "º nome: " + nomes[i])

print("\nLista de nomes invertida:")

for i in range(4,-1,-1):
    print(str(i+1) + "º nome: " + nomes[i])
