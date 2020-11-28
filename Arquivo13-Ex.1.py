def evenCheck(num):
    if num % 2 == 0:
        return 1
    else:
        return 0

x = 1

while x == 1:
    number = int(input("Informe um número inteiro positivo: "))

    if evenCheck(number):
        print("Número par!!")
    else :
        print("Número ímpar!!")
