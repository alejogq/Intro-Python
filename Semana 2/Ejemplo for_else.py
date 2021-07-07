# -*- coding: utf-8 -*-
"""
Created on Thu May 27 10:45:21 2021

@author: alejo
"""

# Only print code if all iterations completed over a list
print('Solo imprime el else si logra llegar al final')
num = int(input('Ingrese un número para probar: '))

for i in range(0, 6):
    if i == num:
        break
    print(i, ' ', end='')
else:
    print()
    print('Se realizaron todas las iteraciones')


if True:
    print("")
else:
    print("s")

    
