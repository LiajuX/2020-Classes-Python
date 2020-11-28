N = list(range(0,5))

for i in range(0,5,1):
    N[i] = input("Nome " + str(i+1) + ": ")

print("Nomes:", N[0], ",", N[1], ",", N[2], ",", N[3], ",", N[4])
print("Nomes:", N[4], ",", N[3], ",", N[2], ",", N[1], ",", N[0])
