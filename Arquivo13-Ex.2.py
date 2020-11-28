def checkUppercase(letter):
    if letter.isupper():
        return "M"
    elif letter.islower():
        return "m"

x = 1

while x ==1:
    letter = input("Informe uma letra maíúscula ou minúscula: ")

    if checkUppercase(letter) == "M":
        print("Letra maiúscula!")
    elif checkUppercase(letter) == "m":
        print("Letra minúscula!")
    else:
        print("O valor informado não é uma letra")
