nota1 = float(input("Informe sua 1ª nota \n"))
nota2 = float(input("Informe sua 2ª nota \n"))
nota3 = float(input("Informe sua 3ª nota \n"))
nota4 = float(input("Informe sua 4ª nota \n"))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 7:
    print("Parabéns você passou de ano com média de %.1f" % media)
elif media > 3:
    print("Você ficou de recuperação e fará exame")
else:
    print("Você foi reprovado!")
