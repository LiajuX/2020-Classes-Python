valorI = int(input("Informe o valor inteiro que deseja calcular o fatorial\n"))

i = 1
fatorial = 1

while i <= valorI:
    fatorial *= i 
    i += 1

print("O fatorial de", valorI, "é", fatorial)
