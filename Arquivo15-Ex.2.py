def compara(t):
    tamanho = len(t)
    if t[0] == t[tamanho - 1]:
        return True
    else:
        return False

t = ()

qtd = int(input("Quantos elementos você quer na tupla? "))

for i in range(qtd):
    t = t + (input("Elemento " + str(i) + ": "),)

if (compara(t)):
    print("O primeiro e o último elemento da tupla são iguais.")
else:
    print("O primeiro e o último elemento da tupla não são iguais.")
            
