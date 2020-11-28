print("Qual o seu nome?");
# Input de dados (Serial.read)
name = input()

# Colocar texto diretamente no input
#(podemos pular linha no input com\n ou tab com\t normalmente)
age = input("Quantos anos você tem?\n")

course= "Engenharia Mecatrônica"

# \t é o tab (4 espaços)
print(name,"tem", age, "anos e está cursando: \n", course, "\tna Fiap")

# Controle de casas decimais
media = 9.56789

print("Média = %.1f" % media)

# Divisão com resultados inteiros: // | Potenciação: **

grade01 = 6.5
grade02 = 9.8
grade03 = 8.5
average = (grade01 + grade02 + grade03) // 3
print(average)

# if - else | Operadores lógicos: and or e not 
if average >= 6 and name == "Júlia":
    print("Parabéns, Júlia! Você passou de ano.")

# elif: condicional encadeado(else if)

i = 0
# while
while i < 5:
    i = i + 1
    print(i)

# Em C: for(i=0; i<=5;i++)
#Em Python: for i in range (0,5,1)
