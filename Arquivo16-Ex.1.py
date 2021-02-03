values = []

def addValues(arrayLen):
    for i in range (arrayLen):
        values.append(input("Insira o " + str(i+1) + "º valor da lista: "))

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

keepGoing = "sim"

while keepGoing == "sim":
    search = input("Insira o valor que deseja pesquisar: ")

    x = searchForValue(values, search)

    if x[0] == True:
        print("Sua pesquisa pelo valor " + search + " foi encontrada na " + str(x[1]+1) + "º posição.")
    else:
        print("Sua pesquisa pelo valor " + search + " não foi encontrada.")

    keepGoing = input("Deseja pesquisar outro valor? Responda com sim ou não.\n")
