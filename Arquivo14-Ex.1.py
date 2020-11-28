M = 5

N = list(range(0,M))

N[M-1] = 0

for i in range(0,M-1,1):
    N[i] = float(input("Nota " + str(i+1) + ": "))
    N[M-1] += N[i]

N[M-1] = N[M-1] / (M-1)

if N[M-1] >= 7:
    print("Você foi aprovado com média de %.1f" % N[M-1])
elif N[M-1] > 3:
    print("Você teve média de %.1f" % N[M-1] + " e ficou de exame")
else:
    print("Você foi reprovado com média de %.1f" % N[M-1])
        
