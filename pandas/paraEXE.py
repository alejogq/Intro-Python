# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 07:49:14 2021

@author: alejo
"""
import pandas as pd
import openpyxl
#Crear una función y calcular una columna nueva
Ventas2=pd.read_excel("VentasEXCEL.xlsx", 
                      engine="openpyxl", 
                      index_col="Producto")
print(Ventas2)

print(Ventas2["Febrero"])

def ganancias(fila):
    return fila["Costo Unidad"]*fila["Num Vendidos"]

def totalvendidos(fila):
    suma=fila["Enero"]+fila["Febrero"]+fila["Marzo"]+fila["Abril"]
    return suma

def total(fila):
    suma=0
    for index in fila.index[1:]:
        suma+=fila[index]
        
    return suma

def totalsem(fila):
    suma=0
    for index in fila.index[6:12]:
        suma+=fila[index]
        
    return suma

# Ventas2["Total ventas"] = Ventas2.apply(gananciasEnero, axis=1)

# Ventas2["Vendidos4"]= Ventas2.apply(totalvendidos,axis=1)

Ventas2["Num Vendidos"] = Ventas2.apply(total, axis=1)
Ventas2["Ingresos Totales"] = Ventas2.apply(ganancias, axis=1)

df=Ventas2.apply(ganancias, axis=1)

suma=df.sum()

print(Ventas2)
# Ventas2.head(10)
