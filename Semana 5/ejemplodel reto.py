# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 13:10:02 2021

@author: alejo
"""
import numpy as np

def solucion(A):
    
    filas = A.shape[0]   ## Hallo el numero de filas
    columnas = A.shape[1]  ## hallo el numero de columnas
    
    filasl = len(A)   ## Hallo el numero de filas
    columnasl = len(A[0])  ## hallo el numero de columnas
  
    
    for i in range(filasl):
        for j in range(columnasl):
            print(A[i][j], end=" ")
        
        print()    
    
    
    return







### calificador


M=np.array([[1,2,4],
            [2,3,5],
            [1,2,4]
            ])

N=np.array([[1,2],
            [1,0]
            ])

s=solucion(M)
print(s)

s=solucion(N)
print(s)
