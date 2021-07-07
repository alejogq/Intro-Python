# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 23:30:15 2021

@author: alejo
"""

#%%
#Creación de un Dataframe

import pandas as pd

from io import StringIO

data = "col1,col2,col3\n4,b,1\n7,3,5\nc,d,3"

archivo="""col1,col2,col3
4,b,1
c,d,3
"""

df=pd.read_csv(StringIO(data))


#%%
#Esquivar datos dentro de la lectura

#df2 = pd.read_csv(StringIO(data), skiprows=[1,3]) #Evitar fila específica
df2 = pd.read_csv(StringIO(data), skiprows=lambda x: x % 2 != 0) #Evitar filas  pares

print(df)
print(df2)

#%%
#poner el header al DF
df3=pd.read_csv(StringIO(data),
                names=["tipo 1", "cantidad ", "otros"],
                header=0) ## Header me referencia la fila que tiene el encabezado
print(df3)


#%%
#Usar solo algunas columnas y ponerles un encabezado (header)

df4=pd.read_csv(StringIO(data),
                usecols=[0, 2],
                names=["Nombre 2", "Nombre 1 "])
print(df4)


#%%
#Usar solo algunas columnas y cambiar el encabezado (header)

df4=pd.read_csv(StringIO(data),
                usecols=[0, 2],
                names=["Nombre 2", "Nombre 1 "],
                skiprows=[0])
print(df4)

#%%

# Definir lineas comentadas en los datos

data2="""A,B,C,D
1,2,3,4
# elementos nuevos del 23 mayo:
10,20,30,40
X,Y,Z,W
1,1,1,1
# Elementos nuevos del 15 junio:
1,2,3,4
x,y,z,w
"""
         
data = "\na,b,c\n  \n# commented line\n1,2,3\n\n4,5,6"

print(data2)

df5=pd.read_csv(StringIO(data2),
                comment="#")
print(df5)

print()
#Puedo cambiar el header
df6=pd.read_csv(StringIO(data2),
                header=2,
                comment="#")
print(df6)

#%%
datos = pd.read_csv("ejemplo.csv")
print(datos)

#%%
datos = pd.read_csv("ejemploEx.csv", sep=";")
print(datos)

#%%
# Abrir archivo csv, es necesario saber la codificación
# Se debe tener en cuenta el delimitador también

Ventas = pd.read_csv("VentasCSV.csv",sep=';')
print(Ventas)

#%%
#Parar leer csv de forma mas general
Ventas = pd.read_csv("ejemploEx_1.csv",delimiter=';', encoding = "ISO-8859-1")
print(Ventas)

#%%
#Llevar a un archivo de excel
Ventas.to_excel("DATOSEXCEL.xlsx", sheet_name="Datos mios")#, index=False)

#%%

#Parar leer excel de forma mas general
Ventas = pd.read_excel(r"VentasExcel_1.xls")
print(Ventas)

#%%
# PARA LEER XLSX, se debe usar openpyxl, ya que xlrd dejó el soporte para XLSX
import openpyxl
#Parar leer csv de forma mas general

Ventas = pd.read_excel(r"VentasExcel.xlsx", engine="openpyxl")
print(Ventas)


#%%

print(Ventas.shape)

#%%
## Filtrar datos, filtrar elementos con costo mayor o igual a 12000

mayores = Ventas[Ventas["Costo Unidad"] <= 5000 ]
mayores.head()

print(mayores)

#%%

mayores = Ventas[Ventas["Abril"].isin([500])]
mayores.head()

print(mayores)

mayores.to_excel("Mayores.xlsx", sheet_name="mayor")


#%%

#Parar leer csv de forma mas general
Ventas2 = pd.read_csv("VentasCSV_NoUTF.csv",
                     delimiter=';',
                     encoding = "ISO-8859-1",
                     index_col="Producto")
print(Ventas2)
print()

fila=Ventas2.iloc[1]
print(fila)
print()

fila=Ventas2.loc["Manzana"]
print(fila)

#%%

## Implementación de filtros, según valores de las columnas

filtro=Ventas2[(Ventas2["Enero"] > 400) & (Ventas2["Marzo"] > 550)]

#%%
import pandas as pd
import openpyxl
#Crear una función y calcular una columna nueva
Ventas2=pd.read_excel("VentasEXCEL.xlsx", 
                      engine="openpyxl", 
                      index_col="Producto")
print(Ventas2)

print(Ventas2["Febrero"])

#%%
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





