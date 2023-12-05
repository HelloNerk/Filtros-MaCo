import numpy as np

def mediana(lista):
    lista.sort()
    pivote=len(lista)
    elemento=0
    if(pivote%2==0):
        posicion1=int(len(lista)/2)
        posicion2=posicion1-1
        elemento=lista[posicion2]+lista[posicion1]
        if(elemento%2==0):
            elemento=elemento/2
        else:
            elemento=int((elemento/2)+0.5)
        return elemento
    else:
        posicion1=round(len(lista)/2)
        elemento=lista[posicion1]
        return elemento
         

n=5

matriz=np.array([[4,5,5,5,3],
                  [3,3,2,4,1],
                  [6,5,3,1,1],
                  [2,2,2,3,4],
                  [7,7,0,4,1]])

nuevamatriz=np.zeros([n,n])
lista=[]

for i in range(n):
    for j in range(n):
        if(i-1>=0 and j-1>=0 ):
            lista.append(matriz[i-1][j-1])
        if(i-1>=0 and j>=0 ):
            lista.append(matriz[i-1][j])
        if(i-1>=0 and j+1<n):
            lista.append(matriz[i-1][j+1])
        if(i>=0 and j-1>=0 ):
            lista.append(matriz[i][j-1])
        if(i+1<n and j-1>=0 ):
            lista.append(matriz[i+1][j-1])
        if(i+1<n  and j>=0 ):
            lista.append(matriz[i+1][j])
        if(i+1<n  and j+1<n ):
            lista.append(matriz[i+1][j+1])   
        if(i>=0  and j+1<n ):
            lista.append(matriz[i][j+1])
        lista.append(matriz[i][j])
        elemento_matriz=mediana(lista)
        nuevamatriz[i][j]=elemento_matriz
        lista.clear()
        
print(nuevamatriz)
                

                    