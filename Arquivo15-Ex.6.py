n = []

def carregaLista(listaLen):
    for i in range (listaLen):
        n.append(int(input("Insira o " + str(i+1) + "º número: ")))

def soma(lista):
    soma = 0
    
    for i in range (len(lista)):
        soma += lista[i]

    return soma

carregaLista(5)

print("Soma  =", soma(n))

for i in range (len(n)):
    print(str(i+1) + "º número:", n[i])
