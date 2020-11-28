def compra(dinheiro,preco):
    qtdBombom = dinheiro // preco
    troco = dinheiro % preco
    return qtdBombom,troco

def maisUmBombom(res,preco):
    dinheiroAMais = preco - res[1]
    return dinheiroAMais
    

dinheiro = float(input("Quantos reais Joãozinho possui? "))
preco = float(input("Quanto custa cada bomobom? "))

res = compra(dinheiro,preco)

print("Joãozinho pode comprar %i bombons." % res[0])
print("E receberá R$ %.2f de troco." % res[1])

mais = maisUmBombom(res,preco)

print("Para comprar mais um bombom Joãozinho precisa pedir mais R$ %.2f para sua mãe." % mais)
