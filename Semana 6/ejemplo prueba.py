import numpy as np

def solucion(A):

    B=[] 
    S=[]
    ## lo uso para encontrar el mínimo
    for i in range(len(A)):
        for j in range (len(A)-i):
            
            if (j+i) % 2 ==1:
                B.append(A[i,j])
                S.append((i,j))
                valor_minimo=min(B)
       
    print(B,S,sep="\n")
    
    posiciones_valor_minimo=[]
    
    for i in range(len(B)):
        if B[i]==valor_minimo:
            posiciones_valor_minimo.append(S[i])
        
    # posiciones_valor_minimo=[]
    ## Lo uso para encontrar las posiciones de valores mínimos
    # for i in range(len(A)):
    #     for j in range (len(A)):
    #         if (j+i) % 2 ==1 and (i+j) <= (len(A)-1) and (A[i,j]==valor_minimo):
                
    #                 posiciones_valor_minimo.append((i,j))
    
      
    
    return valor_minimo, posiciones_valor_minimo


### Estructura para realizar las pruebas

A=np.random.randint(1,10,(4,4))

A=[1,2,3,34,5,6,6,7]

A.sort()

# A = np.array([[4, 3, 9],
#               [8, 9, 2],
#               [8, 7, 2]])

print(A)

a,b = solucion(A)

print(a,b)




