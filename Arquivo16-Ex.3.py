values = []

def addValues(arrayLen):
    for i in range (arrayLen):
        values.append(int(input("Insira o " + str(i+1) + "º valor da lista: ")))

def sortInAscendingOrderAndPrint(array):    
    for i in range(len(array)-1):
        for j in range(i+1, len(array)):
            if array[i] > array[j]:
                x = array[i]
                array[i] = array[j]
                array[j] = x
                
    for i in range(len(array)):
        print(str(i+1) + "º valor da lista: " + str(array[i]))
                

def searchForValue(array, searchedValue):
    found = False
    
    i = 0

    while i < len(array) and found == False:
        if searchedValue == array[i]:
            found = True
        else:
            i += 1

    return found,i

addValues(20)

sortInAscendingOrderAndPrint(values)

keepGoing = "sim"

while keepGoing == "sim":
    search = int(input("Insira o valor que deseja pesquisar: "))

    x = searchForValue(values, search)

    if x[0] == True:
        print("Sua pesquisa pelo valor " + str(search) + " foi encontrada na " + str(x[1]+1) + "º posição.")
    else:
        print("Sua pesquisa pelo valor " + str(search) + " não foi encontrada.")

    keepGoing = input("Deseja pesquisar outro valor? Responda com sim ou não.\n")
