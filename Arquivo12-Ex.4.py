valor = int(input("Informe a quantidade de valores inteiros que deseja somar\n"))

i = 0
soma = 0

while i <= valor:
    soma += i
    i += 1

print("A soma dos", valor, "primeiros números inteiros é", soma)
