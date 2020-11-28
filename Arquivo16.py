n=[]

for i in range(10):
    n.append(input("Nome da pessoa "+str(i+1)+": "))


for i in range(10-1):
    for j in range(i+1,10):
        if n[i]>n[j]:
            x=n[i]
            n[i]=n[j]
            n[j]=x
#impressão
for i in range(10):
    print("Elemento "+str(i+1)+" :",n[i])
RESP='sim'
#pesquisa sequencial
while RESP=='sim':
    pesquisa=input("Qual nome a ser pesquisado?")
    acha=False
    i=0
    while i<10 and acha==False:
        if pesquisa==n[i]:
            acha=True
        else:
            i+=1 #i=i+1
    if acha==True:
        print("Sua pesquisa por "+pesquisa+" foi localizada no elemento: ",i+1)
    else:
        print("Sua pesquisa por "+pesquisa+" não foi localizada!")
    RESP=input("Deseja continuar? Responda com sim ou não.")
print("Pesquisa Encerrada!")
