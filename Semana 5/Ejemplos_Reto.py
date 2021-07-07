#%%
"""
Diferentes formas de pintar una matriz
"""

import numpy as np

def pintarMatriz(a):
        
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            
            if (i+j)%2 !=0: ## detecto una suma impar
                a[i,j]=1
    return a
                
def imprimirMatriz(A):
    print()
    
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            print(A[i,j],end=" ")
        print()
        
def pintarDiagonalSup(A):
    pivote = A.shape[0]## numero de filas
    
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
    
            if j < pivote:
                A[i,j]=1

        pivote=pivote-1        
                
    return A      


def pintarDiagonalInf(A):
    pivote = 0
    
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
    
            if j <= pivote:
                A[i,j]=1

        pivote=pivote+1        
                
    return A


filas=8
columnas=8
A=np.array([[0]*filas]*columnas)
pintarDiagonalSup(A)
imprimirMatriz(A)

B=np.array([[0]*filas]*columnas)
pintarMatriz(B)
imprimirMatriz(B)

D=np.multiply(A,B)
imprimirMatriz(D)

C=np.array([[0]*filas]*columnas)
pintarDiagonalInf(C)
imprimirMatriz(C)

X=np.array.ramdom.randint(1,(3,3))




#%%
"""
Impresion de una matriz
"""
import numpy as np

def imprimirMatriz(A):
    print()
    
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            print(A[i][j],end=" ")
        print()
        
M=np.array([[1, 0, 5, 7], 
            [2, 3, 9, 0],
            [4, 5, 6, 0], 
            [7, 8, 9, 10]]
           )
imprimirMatriz(M)

#%%
"""
Crear un vector con numeros en orden
"""
import numpy as np
def crearVector(tamano):
    vector=[]
    for i in range(1,tamano+1):
        vector.append(i)
    
    vector=np.array(vector)
    return vector

V=crearVector(10)
print(V)

#%%
"""
Repartir un vector en varias listas de diferente tamaño
"""
import numpy as np

def crearVector(tamano):
    vector=[]
    for i in range(1,tamano+1):
        vector.append(i)
    
    vector=np.array(vector)
    return vector

def repartirVector(V):
    fin=False
    indicador=crearVector(len(V))
    M=[]
    posfin=0
    
    for i in indicador:
        lista=[1]*i
        lista[0:i]=V[posfin:posfin+i]
        
        if fin==True:
            break
        
        for j in range(i):
            posfin+=1
            if posfin==len(V):
                fin=True
                break

        M.append(lista)
    
    return M


V=[5,4,6,7,8,4,1,6,3,2]
print(V)

M=repartirVector(V)
print("Vector repartido")
print(M)


#%%
"""
Completar una lista de listas
"""

V=[[5], [8, 8], [2, 8, 6], [1, 1, 1, 2]]

ancho=3
tamano=4

for i in range(tamano):
    faltante = [0]*ancho
    V[i][i+1:] = faltante
    ancho -= 1

print(V)

#%%
"""
Obtención de diagonales
"""

import numpy as np

M=np.array([[1, 0, 5, 7], 
            [2, 3, 9, 0],
            [4, 5, 6, 0], 
            [7, 8, 9, 10]]
           )

print(M)
print()
def obtenerDiagPrin(M):
    V=[]
    for i in range(len(M)):
       V.append(M[i][i]) 
    return V

N=obtenerDiagPrin(M)
print(N)


def obtenerDiagSec(M):
    V=[]
    for i in range(len(M)):
       V.append(M[i][len(M)-i-1]) 
    return V

K=obtenerDiagSec(M)
print(K)
#%%



import numpy as np

def solucion(A):
    
    filas=A.shape[0]
    columnas= A.shape[1]  
    
    print(A[1,0])

    sum_diagonal_principal, prod_diagonal_secundaria, resultado2_mod_resultado1=1,2,3
    
    return sum_diagonal_principal, prod_diagonal_secundaria, resultado2_mod_resultado1

M=np.array([[1,2],[2,3]])

solucion(M)




#%%%

p=[1,2,5,64,7,9,7,5,7,4,5,5,6,7,7,7]

L=len(p)

n=int((-1+np.sqrt(1+8*L))//2) #por ecuacion general

print(n)

X = np.random.randint(0,1,(n,n))
contador=0

for i in range(n):
    contador=contador+1
    for j in range(contador):
        X[i,j]=p[i+j]
             

print(X)

#%%

n=4
X = np.random.randint(1,8,(n,n))
menor=X[0,0]

for i in range(n):
    for j in range(n):
        if ((i+j)%2 !=0 ) and (i+j<n): 
            if X[i,j] < menor:
                menor=X[i,j]

print(X)

#%%
import math

n=4
X = np.random.randint(1,8,(n,n))
menor=X[0,0]
lista=[]
for i in range(n):
    for j in range(n):
        raiz=math.sqrt(X[i,j])
        if raiz%1 == 0:
            lista.append(X[i,j])

print(X)

#%%%
sum=0
for i in range(n):
        print(X[i,i])

print()
mul=1
for i in range(n):
        print(X[i,n-i-1])




