salario = float(input("Qual o seu salário?\n"))
financiamento = float(input("Qual o valor do financiamento desejado?\n"))
prestacao = float(input("Em quantas prestações você deseja pagar o financiamento?\n"))

valor = financiamento / prestacao 

if valor < salario * 0.3:
    print("Seu financiamento foi aprovado!")
else:
    print("Seu crédito não foi aprovado para realizar esse financiamento")
