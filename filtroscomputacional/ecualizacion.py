import numpy as np

lista=[6,12,12,36,24,48,6,6]
totalpixeles=0
for i in lista:
    totalpixeles+=i

print(totalpixeles)
listarelativa=[0,0,0,0,0,0,0,0]

listanueva=[0,0,0,0,0,0,0,0]

for i in range(len(lista)):
    listarelativa[i]=lista[i]/totalpixeles

print(listarelativa)

suma=0
for i in range(len(listarelativa)):
    suma+=listarelativa[i]
    formula=round((8-1)*suma)
    listanueva[formula]+=lista[i]

print(lista)
print(listanueva)    
    