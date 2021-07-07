#!/usr/bin/env python
# coding: utf-8

# <!-- ![imagen_1](listas.png) -->

# <p align="center">
#  
# <img src="listas.png" title="listas" width="500" height="280">
# <div align="center">LISTAS</div>
#  
# </p>

# In[1]:


my_list = ['a', 'c', 'Hello', 18, True]
print(my_list)


# In[2]:


lista=['C','o','l','\'o','m','b','i','a']
longitud=len(lista)
print(f"Longitud de la lista: {longitud}")


# ### Se ordenan comenzando desde el 0

# In[3]:


print(lista[0])
print(lista[len(lista)-1])


# In[4]:


print(lista[1:4])


# ### Se puede acceder al revés usando índices negativos

# In[5]:


print(lista[-1])


# In[6]:


print(lista[-5:-1])


# In[7]:


print(lista[:-3])


# In[8]:


print(lista[:])


# In[9]:


print(lista[4:])


# ### Cambiar datos de una lista

# In[10]:


lista[0]='H'
lista[2]=254
print(lista)


# ### Agregar datos a una lista

# In[11]:


lista.append(254)
lista.append("hola")
lista.append(True)
print(lista)


# ### Eliminar un elemento

# In[12]:


lista.pop(3)
print(lista)


# ### Limpiar la lista

# In[13]:


lista.clear()
print(lista)


# <p align="center">
#  
# <img src="tuplas.png" title="listas" width="500" height="280">
# <div align="center">TUPLAS</div>
#  
# </p>

# In[14]:


num=(1,)
numeros=(1,3,5,7,9,11)
vocales=('a','e','i','o','u')


# In[15]:


print(numeros[3])
print(vocales[2:4])


# In[16]:


numeros=numeros+(13,15,19)
print(numeros)


# In[17]:


numeros=numeros*2
print(numeros)


# ### NO se pueden eliminar datos de una tupla, solo añadir

# <p align="center">
#  
# <img src="sets.png" title="listas" width="500" height="280">
# <div align="center">SETS</div>
#  
# </p>

# In[18]:


con={1,2,"hola", True,2}
print(con)


# In[19]:


numeros={1,2,3,5,4}
frutas={"manzana", "peras","higos"}


# In[20]:


tienda=numeros.union(frutas)
print(tienda)


# In[21]:


print('higos' in tienda)


# In[22]:


nuevo=tienda.intersection(frutas)
print(nuevo)


# In[23]:


dif=tienda.difference(frutas)
print(dif)


# In[24]:


simdif=tienda.symmetric_difference(frutas)
print(simdif)


# ### No se puede modificar el dato específico de un set

# In[25]:


tienda.add("uvas")
print(tienda)


# In[26]:


tienda.remove('higos')
print(tienda)


# In[27]:


## elimina un elemento arbitrario y lo devuelve
tienda.pop()


# In[28]:


tienda.clear()
print(tienda)


# <p align="center">
#  
# <img src="diccionarios.png" title="listas" width="500" height="280">
# <div align="center">DICCIONARIO</div>
#  
# </p>

# In[29]:


diccionario={
    "Peras":20,
    "manzanas": 2    
}

print(diccionario)


# In[30]:


diccionario["Peras"]


# In[41]:


autos ={
  "marca": "mazda",
  "asegurado": False,
  "año": 1964,
  "colores": ["red", "white", "blue"]
}


# In[45]:


print(autos)


# In[46]:


print(autos["colores"][2])


# <p align="center">
#  
# <img src="preguntas.png" title="listas" width="500" height="280">
# <div align="center">LISTAS</div>
#  
# </p>

# ## Datos Anidados

# ### Anidación en diccionarios

# In[16]:


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


# In[2]:


libro["capitulo 1"]


# In[3]:


libro['capitulo 1']["paginas"]


# In[4]:


libro["capitulo 1"]["Titulos"].append("tema 4")
print(libro["capitulo 1"]["Titulos"][2])


# In[5]:


### Cambiar un elemento a cualquier nivel
libro["capitulo 1"]="Ejemplo"
print(libro)


# In[6]:


### Añadir elementos
libro["capitulo 3"]={"ilustraciones":0, "paginas":15}
print(libro)


# In[7]:


del libro["capitulo 2"]["ilustraciones"]
print(libro)


# In[8]:


libro.pop("capitulo 2")


# ### Anidación de Tuplas

# In[19]:


tuplas=(1,2,3,('a','b','c',(3,5,6)))


# In[21]:


tuplas[3][3][2]


# In[1]:


tupla=(1,2,3,["a","b"],{"cancion":"cry","duracion":15},{2,3,5,7})
print(tupla)


# In[2]:


tupla[3][1]


# In[3]:


tupla[4]["cancion"]


# In[4]:


type(tupla)


# ### Anidacion en Listas

# In[33]:


lista= [1,2,3,4,["blanco","negro","azul",["azul-verde","azul-morado"]]]


# In[34]:


print(lista)


# In[35]:


lista[4][3][0]


# In[38]:


lista_dicc=["hola",1,2,{"elemento":1,"causa":2}]
print(lista_dicc)


# In[40]:


lista_dicc[3]["elemento"]


# ### Anidacion sets: solo pueden anidar tuplas

# In[23]:


b={1,2,4,4,5}


# In[16]:


a={1,2,4,(1,2)} 


# In[24]:


a.intersection(b)


# In[27]:


## ERRRORES:
a={1,2,4,[1,2]} ## error
a={1,2,4,{1,2}} ## error
a={1,2,4,{"num1":1,"num2":2}} ## error


# ### Recorrido y creación de estructuras de datos

# In[28]:


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


# In[29]:


print(datos)


# In[ ]:


a=0
b=2
if (a==1) and (b==2):
    print("no es lo que se buscaba")
elif (a==0) and (b==2): 
    print("Es correcto")
    print("asdasd")
    


# ### Por Comprension

# In[1]:


languages = ["python", "c", "c++", "java"]


# In[2]:


cap_languages = [language.capitalize() for language in languages]


# In[3]:


cap_languages


# In[4]:


numeros=[1,2,3,5,5]
doblar_num = [n * 2 for n in numeros]


# In[5]:


doblar_num


# In[7]:


### Esquema para la creación de este tipo de sentencias
### [expresion for variable in colección if condición]


# In[8]:


points = [(x, y) for y in range(0, 5 + 1) for x in range(0, 10 + 1)]
print(points)


# In[ ]:

p=0

    


