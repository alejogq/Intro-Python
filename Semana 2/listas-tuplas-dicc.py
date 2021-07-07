#!/usr/bin/env python
# coding: utf-8
# %% [markdown]
#
# # <!-- ![imagen_1](listas.png) -->
#
# # <p align="center">
# #  
# # <img src="listas.png" title="listas" width="500" height="280">
# # <div align="center">LISTAS</div>
# #  
# # </p>

# %%





# %%
lista_1 = ['a', 'c', 'Hello', 18, True]
print(lista_1)


# %%
lista_1[4]


# %%
lista=['C','o','l','o','m','b','i','a']

longitud=len(lista)
print(f"Longitud de la lista: {longitud}")


# %%
lista


# ### Se ordenan comenzando desde el 0

# %%
print(lista[0])
print(lista[len(lista)-1])


# %%
print(lista[0:4])

# ### Se puede acceder al revés usando índices negativos

# %%


print(lista[-1])
    


# %%


print(lista[-5:-1])


# %%


print(lista[:-3])


# %%


print(lista[:])


# %%


print(lista[4:])

   
    
# ### Cambiar datos de una lista

# %%


lista[0]='H'
lista[2]=254
print(lista)


# %%


lista[5]=1


# ### Agregar datos a una lista

# %%


lista.append(254)
lista.append("hola")
lista.append(True)
print(lista)


# ### Eliminar un elemento

# %%


lista.pop(3)
print(lista)


# ### Limpiar la lista

# %%


lista.clear()
print(lista)


# %%


numeros=[1,2,3,56]


# %%


total=numeros[1]*numeros[3]
print(total)


# %% [markdown]
#
#
# print(len(numeros))
#
#
# # <p align="center">
# #  
# # <img src="tuplas.png" title="listas" width="500" height="280">
# # <div align="center">TUPLAS</div>
# #  
# # </p>

# %%


num=(1,)
numeros=(1,3,5,7,9,11,'2')
vocales=('a','e','i','o','u')


# %%


numero=(1)


# %%


print(num)


# %%


numeros


# %%


print(vocales[4])


# %%


print(numeros[3])
print(vocales[2:-1])


# %%


numeros=numeros+(13,15,19)
print(numeros)


# %% [markdown]
#
#
# numeros=numeros*2
# print(numeros)
#
#
# # ### NO se pueden eliminar datos de una tupla, solo añadir
#
# # <p align="center">
# #  
# # <img src="sets.png" title="listas" width="500" height="280">
# # <div align="center">SETS</div>
# #  
# # </p>

# %%


con={1,2,"hola", True,'2',2.1}
print(con)


# %%


numeros={1,2,3,5,4}
frutas={"manzana", "peras","higos"}


# %%


tienda=numeros.union(frutas)
print(tienda)


# %%


print('higos' in tienda)


# %%


nuevo=tienda.intersection(frutas)
print(nuevo)


# %%


dif=tienda.difference(frutas)
print(dif)


# %%


num={1,2,3,4,5,6,7}
num2={5,6,7,8}
simdif=num.symmetric_difference(num2)
print(simdif)


# ### No se puede modificar el dato específico de un set

# %%


tienda.add("uvas")
print(tienda)


# %%


tienda.remove('higos')
print(tienda)


# %%


## elimina un elemento arbitrario y lo devuelve
tienda.pop()


# %% [markdown]
#
#
# tienda.clear()
# print(tienda)
#
#
# # <p align="center">
# #  
# # <img src="diccionarios.png" title="listas" width="500" height="280">
# # <div align="center">DICCIONARIO</div>
# #  
# # </p>
#
# # ## CLASE de recuperación: Lunes de 12:2 pm

# %%


diccionario={"Peras"   : 20,
             "manzanas": 2,
             "Higos"   : 24,
             "papitas" : 20
            }

print(diccionario)


# %%


diccionario["Peras"]=30


# %%


diccionario["Peras"]


# %%


diccionario.pop("Peras")
diccionario


# %%


diccionario["garbanzos"]=20
diccionario


# %%


diccionario.popitem()
diccionario


# %%


diccionario={
    "Peras":20,
    "manzanas": 2    
}

diccionario["Higos"]=40
diccionario


# %%


del diccionario["Higos"]


# %%


diccionario


# %%


nuevo=diccionario.fromkeys("Peras")


# %%


for i in nuevo:
    print(i)


# %%


q=diccionario.get("carros")
print(q)


# %%


diccionario["carros"]


# %%


a=diccionario.items()
a


# %%


colores=["rojo", "blanco", "azul"]

autos = {
  "marca"     : "mazda",
  "asegurado" : False,
  "año"       : 1964,
  "colores"   : colores
  }


# %%


print(autos)


# %%


print(autos["colores"])


# %%


diccionario = {'color': 'rosa', 'marca': 'Zara', 'talle': 'U'} 
for clave, valor in diccionario.items(): 
    print("El valor de la clave %s es %s" %(clave, valor))


# %%


diccionario.values()


# %%


len(diccionario)


# <p align="center">
#  
# <img src="preguntas.png" title="listas" width="500" height="280">
# <div align="center">LISTAS</div>
#  
# </p>

# ## Datos Anidados

# ### Anidación en diccionarios

# %%


libro={
    "capitulo 1": {
        "paginas": 20,
        "ilustraciones": 12,
        "Titulos":["tema 1", "tema 2", "tema 3", {"sesion especial":"agradecimientos","autores":"Juan, David" }]
        
        },
    "capitulo 2":{
        "paginas":12,
        "ilustraciones":2
        
        }
    
}


# %%


libro["capitulo 1"]


# %%


libro['capitulo 1']["paginas"]


# %%


libro["capitulo 1"]["Titulos"].append("tema 4")
print(libro["capitulo 1"]["Titulos"][2])


# %%


### Cambiar un elemento a cualquier nivel
libro["capitulo 1"]="Ejemplo"
print(libro)


# %%


### Añadir elementos
libro["capitulo 3"]={"ilustraciones":0, "paginas":15}
print(libro)


# %%


del libro["capitulo 2"]["ilustraciones"]
print(libro)


# %%


libro.pop("capitulo 2")


# ### Anidación de Tuplas

# %%


tuplas=(1,2,3,('a','b','c',(3,5,6)))


# %%


tuplas[3][3][2]


# %%


tupla=(1,2,3,["a","b"],{"cancion":"cry","duracion":15},{2,3,5,7})
print(tupla)


# %%


tupla[3][1]


# %%


tupla[4]["cancion"]


# %%


type(tupla)


# ### Anidacion en Listas

# %%


lista= [1,2,3,4,["blanco","negro","azul",["azul-verde","azul-morado"]]]


# %%


print(lista)


# %%


lista[4][3][0]


# %%


lista_dicc=["hola",1,2,{"elemento":1,"causa":2}]
print(lista_dicc)


# %%


lista_dicc[3]["elemento"]


# ### Anidacion sets: solo pueden anidar tuplas

# %%


b={1,2,4,4,5}


# %%


a={1,2,4,(1,2)} 


# %%


a.intersection(b)


# %%


## ERRRORES:
a={1,2,4,[1,2]} ## error
a={1,2,4,{1,2}} ## error
a={1,2,4,{"num1":1,"num2":2}} ## error


# ### Recorrido y creación de estructuras de datos

# %%


datos=[]
while(True):
    nombre=input("ingrese nombre")
    edad=input("ingrese edad")
    dato={
        'nombre':nombre,
        'edad':edad
    }
    datos.append(dato)
    opcion=input("¿Desea ingresar un dato nuevo? (s/n)" )
    if opcion=='n':
        break

for i in datos:
    print(i['nombre'])
    print(i['edad'])
    
print(datos)  


# %%


print(datos)


# %%


a=0
b=2
if (a==1) and (b==2):
    print("no es lo que se buscaba")
elif (a==0) and (b==2): 
    print("Es correcto")
    print("asdasd")
    


# ### Por Comprension

# %%


dicc={j for j in range(9)}


# %%


[k for k in range(10) if k%2==0]


# %%


languages = ["python", "c", "c++", "java"]


# %%


cap_languages = [language.capitalize() for language in languages]


# %%


cap_languages


# %%


numeros=[1,2,3,5,5]
doblar_num = [n * 2 for n in numeros]


# %%


doblar_num


# %%


### Esquema para la creación de este tipo de sentencias
### [expresion for variable in colección if condición]


# %%


points = [(x, y) for y in range(0, 5 + 1) for x in range(0, 10 + 1)]
print(points)


# %%


get_ipython().run_cell_magic('capture', '', "Diccionario={1: {'y_0': 1.0,   'y_1': 1.0,   'y_2': 0.0,   'y_3': 1.0,   'y_4': 1.0,   'y_5': 0.0,   'y_6': 1.0,   'y_7': 1.0,\n  'y_8': 1.0,   'x_0': 0.0,   'x_2': 1.0,    'x_7': 0.0,  'c1a_0@int_slack@0': 0.0,  'c1a_1@int_slack@0': 1.0,\n  'c1a_1@int_slack@1': 0.0,  'c1a_2@int_slack@0': 0.0,  'c1a_3@int_slack@0': 0.0,  'c1a_4@int_slack@0': 0.0,\n  'c1a_5@int_slack@0': 0.0,  'c1a_6@int_slack@0': 0.0,  'c1a_7@int_slack@0': 0.0,  'c1a_8@int_slack@0': 0.0,\n  'valor': 25.0,   'tiempo': 39.533639907836914}, \n 2: {'y_0': 1.0,  'y_1': 1.0,   'y_2': 0.0,  'y_3': 1.0,  'y_4': 1.0,  'y_5': 0.0,  'y_6': 1.0,  'y_7': 1.0,\n  'y_8': 1.0,  'x_0': 0.0,  'x_2': 1.0,  'x_7': 0.0,  'c1a_0@int_slack@0': 0.0,  'c1a_1@int_slack@0': 1.0,  'c1a_1@int_slack@1': 0.0,\n  'c1a_2@int_slack@0': 0.0,  'c1a_3@int_slack@0': 0.0,  'c1a_4@int_slack@0': 0.0,  'c1a_5@int_slack@0': 0.0,\n  'c1a_6@int_slack@0': 0.0,  'c1a_7@int_slack@0': 0.0,  'c1a_8@int_slack@0': 0.0,  'valor': 25.0,  'tiempo': 31.193804502487183}}")


# %%
keys= list(Diccionario[1].keys())


# %%
Diccionario_2={i:{key:Diccionario[i][key] for key in keys } for i in Diccionario}

