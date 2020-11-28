N = list(range(0,6))

N[5] = 0

for i in range (0,5,1):
    N[i] = int(input("Insira o número " + str(i+1) + ": "))
    N[5] += N[i]

print("Soma dos números informados = ", N[5])
print("1º número", N[0])
print("2º número", N[1])
print("3º número", N[2])
print("4º número", N[3])
print("5º número", N[4])
