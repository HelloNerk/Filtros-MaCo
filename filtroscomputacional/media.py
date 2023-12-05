import numpy as np
        
mascara=np.array([[1,2,1],[2,4,2],[1,2,1]])

fraccion=(1/16)

n=5

matriz= np.array([[1,0,2,2,0],
                  [7,3,3,4,1],
                  [4,5,0,7,3],
                  [1,1,1,3,5],
                  [1,6,1,4,2]])
nuevamatriz=np.zeros([n,n])

            

for i in range(n):
    for j in range(n):
        temp=0
        if(i-1>=0 and j-1>=0 ):
            temp+=matriz[i-1][j-1]*mascara[0,0]
        if(i-1>=0 and j>=0 ):
            temp+=matriz[i-1][j]*mascara[0,1]
        if(i-1>=0 and j+1<n):
            temp+=matriz[i-1][j+1]*mascara[0,2]
        if(i>=0 and j-1>=0 ):
            temp+=matriz[i][j-1]*mascara[1,0]
        if(i+1<n and j-1>=0 ):
            temp+=matriz[i+1][j-1]*mascara[2,0]
        if(i+1<n  and j>=0 ):
            temp+=matriz[i+1][j]*mascara[2,1]
        if(i+1<n  and j+1<n ):
            temp+=matriz[i+1][j+1]*mascara[2,2]  
        if(i>=0  and j+1<n):
            temp+=matriz[i][j+1]*mascara[1,2]
        temp+=matriz[i][j]*mascara[1,1]
        nuevamatriz[i][j]=round(fraccion*temp)
        
print(nuevamatriz)
                