t = ()

def inverte(tupla):
    novaTupla = ()

    for i in range(2,-1,-1):
         novaTupla = novaTupla + (tupla[i],)

    return novaTupla
        

for i in range (3):
    t = t + (input(str(i+1) + "º elemento da tupla: "),)

print("Tupla invertida:", inverte(t))
