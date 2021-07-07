# -*- coding: utf-8 -*-
"""
Created on Fri May 28 09:41:32 2021

@author: alejo
"""

operacion = input("Ingrese operación")
numero1   = int(input("Numero  1: "))
numero2   = int(input("Numero  2: "))


if operacion == "suma":
    resultado=numero1+numero2
    print(f"{operacion}= ", resultado)

elif operacion == "resta":
    print(f"{operacion}={numero1-numero2} ")

elif operacion == "division":
    print(f"{operacion}={numero1/numero2} ")

elif operacion == "multiplicacion":
    print(f"{operacion}={numero1-numero2} ")

elif operacion == "Potencia= ":
    print(f"{operacion}={numero1-numero2} ")



