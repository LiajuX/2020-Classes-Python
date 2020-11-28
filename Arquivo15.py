dados = input("Informe as notas: ")

n = list(map(float, dados.split()))

t = len(n)

S = 0

for i in range(0,t,1):
    S += n[i]

n.append(S/(t))

if n[t]>=7:
    print("Aprovado! Média: %.1f" % n[t])
elif n[t]>=3:
    print("Em exame! Média: %.1f" % n[t])
else:
    print("Reprovado! Média: %.1f" % n[t])
