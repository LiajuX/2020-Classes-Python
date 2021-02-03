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
                

def binarySearch(array, searchedValue):
    found = False
    
    start = 0
    finish = len(array) - 1

    while start <= finish and found == False:
        half = (start + finish) // 2
        
        if searchedValue == array[half]:
            found = True
        else:
            if searchedValue < array[half]:
                finish = half - 1
            else:
                start = half + 1

    return found,half

addValues(20)

sortInAscendingOrderAndPrint(values)

keepGoing = "sim"

while keepGoing == "sim":
    search = int(input("Insira o valor que deseja pesquisar: "))

    x = binarySearch(values, search)

    if x[0] == True:
        print("Sua pesquisa pelo valor " + str(search) + " foi encontrada na " + str(x[1]+1) + "º posição.")
    else:
        print("Sua pesquisa pelo valor " + str(search) + " não foi encontrada.")

    keepGoing = input("Deseja pesquisar outro valor? Responda com sim ou não.\n")
