# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 14:42:52 2021

@author: alejo
"""

num=int(input("numero: "))

maximo=str(num)*num
maximo=len(maximo)

mitad=int((maximo*1.5))

for i in range(1,num+1):
    if i < 10:
       
        espacio = (mitad+2)*" "
        texto=(str(i)+"   ")*i
        print(espacio + texto)
        mitad=mitad-2
    elif i==10:
        # print()
        espacio = (mitad+2)*" "
        texto=(str(i)+"  ")*i
        print(espacio + texto)
    
        mitad=mitad-2
    else:
        espacio = (mitad+2)*" "
        texto=(str(i)+"  ")*i
        print(espacio + texto)
    
        mitad=mitad-2





