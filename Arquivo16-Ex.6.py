students = []

def addStudents():
    while True:
        students.append(input("Insira o nome do " + str(len(students)+1) + "º estudante: "))

        addNewStudent = input("Deseja inserir o nome de um novo aluno na lista? Responda com sim ou não.\n")

        if addNewStudent != "sim":
            break

def sortInAscendingOrderAndPrint(array):
    for i in range(len(array)-1):
        for j in range (i, len(array)):
            if array[i] > array[j]:
                x = array[i]
                array[i] = array[j]
                array[j] = x

    for i in range (len(array)):
        print("Aluno número " + str(i+1) + ": " + array[i])

def binarySearch(array, searchedName):
    found = False
    
    start = 0
    finish = len(array) - 1

    while start <= finish and found == False:
        half = (start + finish) // 2
        
        if searchedName == array[half]:
            found = True
        else:
            if searchedName < array[half]:
                finish = half - 1
            else:
                start = half + 1 

    return found,half

addStudents()

sortInAscendingOrderAndPrint(students)

keepGoing = "sim"

while keepGoing == "sim":
    search = input("Insira o nome do aluno que deseja buscar: ")

    x = binarySearch(students, search)

    if x[0] == True:
        print("O(A) aluno(a) " + search + " foi encontrado(a) na " + str(x[1]+1) + "º posição da lista.")
    else:
        print("O(A) aluno(a) " + search + " não foi encontrado(a) na lista.")

    keepGoing = input("Deseja pesquisar o nome de outro aluno? Responda com sim ou não.\n")
