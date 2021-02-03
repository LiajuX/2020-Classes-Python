matrizA = []

def carregaMatrizA(matriz, matrizLen):
    for i in range(matrizLen):
        matriz.append(int(input("Insira o " + str(i+1) + "º número inteiro: "))) 

def criaMatrizAoCubo(matriz):
    matrizAoCubo = []
    
    for i in range (len(matriz)):
        matrizAoCubo.append(matriz[i]**3)

    return matrizAoCubo

carregaMatrizA(matrizA, 30)

print("Matriz A:", matrizA)

print("Matriz B:", criaMatrizAoCubo(matrizA))
