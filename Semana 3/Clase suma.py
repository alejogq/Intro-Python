# -*- coding: utf-8 -*-
"""
Created on Mon May 31 17:00:33 2021

@author: alejo
"""

def suma():
    a=int(input("Numero a: "))
    b=int(input("Numero b: "))
    sumar=a+b
    
    return sumar

print("Suma entradas: ",suma())

def suma(a,b):
    sumar=a+b
    return sumar


print("suma 2: ",suma(8,3))
