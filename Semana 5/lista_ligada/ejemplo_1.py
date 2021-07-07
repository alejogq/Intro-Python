from lista_ligada import *

nodo1 = nodoSimple("D")
nodo2 = nodoSimple("I")
nodo3 = nodoSimple("A")
nodo4 = nodoSimple("O")

nodo1.asignarLiga(nodo2)
nodo2.asignarLiga(nodo3)
nodo3.asignarLiga(nodo4)

#%%

#imprimimos el dato guardado en nodo1
print(nodo1.retornarDato())

#Asignamos a siguiente el objeto tipo nodoSimple guardado en nodo1.liga
siguiente = nodo1.retornarLiga()

#Imprimimos el dato guardado en siguiente, que es equivalente a nodo 2
print(siguiente.dato)

#Asignamos a siguiente el objeto que se encuentra en siguiente.liga, que es el nodo 3
siguiente = siguiente.liga

#Imprimimos el dato guardado en nodo 3, que es lo que está guardado en siguiente
print(siguiente.retornarDato())

#Asignamos a siguiente el objeto que se encuentra en siguiente.liga, que es el nodo 3
siguiente = siguiente.liga

#imprimo el ultimo dato
print(siguiente.retornarDato())


#%%
from lista_ligada import *
nodo1=nodoSimple("Hola, ")
nodo2=nodoSimple("¿como ")


nodo3=nodoSimple("estás?")

nodo1.asignarLiga(nodo2)
nodo2.asignarLiga(nodo3)

#%%
"""
Recorrido por la lista ligada
"""
siguiente=nodo1

while siguiente != None:
    print(siguiente.retornarDato(), end="")
    siguiente = siguiente.liga
    


#%%
a=nodo1.retornarDato()



#%%

nodo1=nodoSimple("Hola, ")
nodo2 = nodoSimple("¿Cómo ")
nodo3=nodoSimple("estas ")


nodo4=nodoSimple("tú?")

## Ligo el nodo 1 con el nodo 2
nodo1.asignarLiga(nodo2)
nodo2.asignarLiga(nodo3)
nodo3.asignarLiga(nodo4)

print(nodo1.dato, end="")
nuevaLiga = nodo1.liga

while nuevaLiga != None:
    
    print(nuevaLiga.dato, end="")
    
    nuevaLiga = nuevaLiga.liga



