import numpy as np

lista=[0,15,45,21,51,12,0,0]
lista2=[0,0,0,0,0,0,0,0]
menor=1 #valor del grafico original
mayor=5 #valor del grafico original
newmayor=7 #el valor al que quieres ampliar
newmenor=0 #el valor al que quieres ampliar
pendiente=(newmayor-newmenor)/(mayor-menor)
#momentaneo
mr=menor*pendiente
mr*=-1
#momentaneo
tr=newmenor
#fijo
b=tr+mr

for i in range(len(lista)):
    if(lista[i]!=0):
        formula=round((pendiente*i)+b)
        lista2[formula]=lista[i]


print(lista)
print(lista2)