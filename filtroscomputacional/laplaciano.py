import numpy as np
        
mascara=np.array([[-1,-2,-1],
                  [0,0,0],
                  [1,2,1]])

n=4

matriz=np.array([[4,4,3,2],
                  [7,7,6,6],
                  [4,1,2,3],
                  [2,5,1,2]])
 
menor=0  #original
mayor=7  #original

nuevamatriz=np.zeros([n,n])

for i in range(n):
    for j in range(n):
        temp=0
        if(i-1>=0 and j-1>=0 ):
            temp+=(matriz[i-1][j-1]*mascara[0][0]) 
        if(i-1>=0 and j>=0 ):
            temp+=(matriz[i-1][j]*mascara[0][1])
        if(i-1>=0 and j+1<n):
            temp+=(matriz[i-1][j+1]*mascara[0][2])
        if(i>=0 and j-1>=0 ):
            temp+=(matriz[i][j-1]*mascara[1][0])
        if(i>=0  and j+1<n):
            temp+=(matriz[i][j+1]*mascara[1][2])
        if(i+1<n and j-1>=0 ):
            temp+=(matriz[i+1][j-1]*mascara[2][0])
        if(i+1<n and j>=0 ):
            temp+=(matriz[i+1][j]*mascara[2][1])
        if(i+1<n  and j+1<n ):
            temp+=(matriz[i+1][j+1]*mascara[2][2])
        temp+=(matriz[i][j]*mascara[1][1])
        nuevamatriz[i][j]=temp

newmenor=nuevamatriz[0][0]
newmayor=nuevamatriz[0][0]

for i in range(n):
    for j in range(n):
        if(nuevamatriz[i][j]<=newmenor):
            newmenor=nuevamatriz[i][j]
        if(nuevamatriz[i][j]>=newmayor):
            newmayor=nuevamatriz[i][j]

#T(r)=m*r + b
#m=y2-y1/x2-x1

pendiente=(mayor-menor)/(newmayor-newmenor)

print(pendiente)
#momentaneo
mr=newmenor*pendiente
mr*=-1
#momentaneo
tr=menor
#fijo
b=tr+mr

print(b)

filtrada=np.zeros([n,n])

for i in range(n):
    for j in range(n):
        formula1=(pendiente*nuevamatriz[i][j])+b
        formula=round((pendiente*nuevamatriz[i][j])+b)
        filtrada[i][j]=formula




print(nuevamatriz)
print(filtrada)