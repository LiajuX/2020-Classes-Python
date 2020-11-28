valor = int(input("Informe quantos valores da série deseja ver\n"))

# c = a + b 

a = 1
b = 1

for i in range (0,valor,1):
    print(b)
    c = a + b
    b = a
    a = c
    
