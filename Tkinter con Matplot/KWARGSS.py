# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 11:05:47 2021

@author: alejo
"""

"""
     *args: es una lista de argumentos, como argumentos posicionales.
 
     **kwargs: es un diccionario cuyas claves se convierten en parámetros 
     y sus valores en los argumentos de los parámetros.
"""
#%%
def read_list_args(*args):
    for count, arg in enumerate(args):
        print('%d - %s'%(count, arg))


def imprimirParametros(*parametros):
    for i in parametros:
        print(i)
        

print('Caso 1')
read_list_args('Ricardo', 'Daniel')

print('\nCaso 1-A')
lista=["richard","Pedro"]
imprimirParametros(lista)

print('\nCaso 2')
read_list_args('Ricardo', 23, 'Ramon', [1, 2, 3])

print('\nCaso 2-A')
imprimirParametros('Ricardo', 23, 'Ramon', [1, 2, 3])

#%%

def read_dict_args(**kwargs):
    for key, value in kwargs.items():
        print('%s - %s' % (key, value))
    print("se ejecuto")

def leerDiccParam(**ParamDicc):
    for key, value in ParamDicc.items():
        print('%s - %s' % (key, value))
        
        if key == "Jugador":
            print("Hola")
            

print('Caso 1')
read_dict_args()

print('\nCaso 1-A')
leerDiccParam(name1='Ricardo', name2='Ramon')

print('\nCaso 2')
read_dict_args(Equipo='FC Barcelona', Jugador='Iniesta', Posicion='Banda Derecha', Numero=8)
print('\nCaso 2-A')
leerDiccParam(Equipo='FC Barcelona', Jugador='Iniesta', Posicion='Banda Derecha', Numero=8)



