# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 13:58:38 2021

@author: alejo
"""


import pandas as pd

## Leo el archivo y lo guardo en el dataframe que se llama data
data = pd.read_csv("GOOG.csv", header=0)

data["Promedio"]=""
data["Promedio"]=(data["High"] + data["Low"])/2


#Se crear una nueva columana dentro del dataframe
data["Concepto"]=""

## Se llenan los datos en la columnda Concepto según cada filtro
data["Concepto"][(data["Close"] < 1624)]="MUY BAJO"
data["Concepto"][(data["Close"] >= 1624) & (data["Close"] < 1854)]="BAJO"
data["Concepto"][(data["Close"] >= 1854) & (data["Close"] < 2084)]="MEDIO"
data["Concepto"][(data["Close"] >= 2084) & (data["Close"] < 2314)]="ALTO"
data["Concepto"][(data["Close"] >= 2314)]="MUY ALTO"

##vamos a crear el archivo
data.to_csv("analisis_archivo.csv",
            sep="\t", 
            columns=["Date","Concepto"],
            header=["Fecha", "Concepto"],
            index=False)

## se crea una columna nueva con elnombre de promedio

## Se busca el dato mayor
mayor=data["Promedio"].max()
menor=data["Promedio"].min()
lowest_mean=menor
highest_mean=mayor

## Se busca el dato menor
# fechamayor2=data["Date"][data["Promedio"].idxmax]
# fechamenor2=data["Date"][data["Promedio"].idexmin]

fechamayor = data["Date"][data["Promedio"]==mayor]
fechamenor = data["Date"][data["Promedio"]==menor]

# date_lowest_mean=fechamenor[fechamenor.index[0]]
# date_highest_mean=fechamayor[fechamayor.index[0]]




#%%
