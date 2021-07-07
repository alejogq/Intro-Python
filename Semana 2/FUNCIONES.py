#!/usr/bin/env python
# coding: utf-8

# ### Funciones Vacias

# In[7]:


def sumar(a,b):
    pass

def restar(a,b):
    pass

def ecuacion(a,b):
    a=sumar(2,1)
    b=restar(3,3)
    return a


# In[8]:


print(ecuacion(2,3))


# In[ ]:





# ## Retornar diferentes elementos

# In[ ]:


def intento(a,b):
    if a==0:
        return 
    elif a==2:
        return a
    else:
        print("hola")


# In[ ]:


intento(1,0)


# In[ ]:


intento(0,1)


# In[ ]:


intento(2,1)


# In[ ]:


def hola(arg):
    """Este es el docstring de la función"""
    print("Hola", arg, "!")


# In[ ]:


help(hola)


# In[ ]:


print(hola.__doc__)


# ### Funciones dentro de funciones

# In[9]:


def sumas(a,b):
    
    def suma1(a,b):
        return a+2*b
    
    return suma1(2,3)+a+b

sumas(4,5)


# In[10]:


suma1(2,3)


# In[11]:


def print_msg(number):
    def printer():
        "Aqui estamos usando la palabra clave nolocal"
        nonlocal number
        number=3
        print(number)
    printer()
    number=number+1
    print(number)

print_msg(9)


# In[ ]:





# ### Valores por defecto de las variables

# In[12]:


def suma(a=0,b=0):
    return a+b

def suma_2(a,b):
    return a+b


# In[15]:


suma(1,3)


# In[ ]:


#### Arroja un errror
suma_2()


# ### Variables locales y Globales

# In[ ]:


x=2
def suma(a,b):
    x=5
    suma=a+b+x
    print("x= ", x)
    return suma

suma(3,5)
print("x=",x)


# In[ ]:


x=2
def suma(a,b):
    global x
    x=5
    suma=a+b+x
    print("x= ", x)
    return suma

suma(3,5)
print("x=",x)


# In[ ]:


suma(2,3)


# ### En el siguiente ejemplo la variable global no puede ser cambiada

# In[17]:


def duplicar(x):
    x = x*2

x = 10
duplicar(x)
print(x)


# ### Definimos la variable x como global para poder hacer el cambio

# In[16]:


def duplicar():
    global x
    x = x*2

x = 10
duplicar()
print(x)


# ## Variables no Locales

# La variable a toma su valor de una subrutina mayor pero no es global, entonces se dice no local.

# In[12]:


def rutina(a):
    
    def subrutina():
        nonlocal a
        a = 3
        print(a)
        return

    subrutina()
    
    print(a)
    return

a = 4
rutina(a)
print(a)


# In[20]:


variable=20

def funcion1():
    def funcion_interna():
        global variable
        variable=0
    funcion_interna()

funcion1()
print(variable)


# In[ ]:





# #### Realizar una función que retorne el cuadrado de un número

# In[ ]:


numeroglobal = 20

def cuadrado(numero=10, numero2=0):
    """Esta es una función que calcula el cuadrado de un número"""
    global numeroglobal
    numcuad = numero**2  ## Variable interna
    num2=numero2**2
    numeroglobal=numeroglobal*2
    return numeroglobal, numcuad

def minimo():
    global numeroglobal
    numeroglobal=0


# In[ ]:


lista = []
lista = cuadrado()


# In[ ]:


lista


# In[ ]:


print(var1)
print(var2)


# In[ ]:


numeroglobal


# In[ ]:


var,var1 = cuadrado(10,20)


# In[ ]:


print(var, var1)


# In[ ]:


print(numcuad)


# ## Importación de funciones

# In[1]:


import sumar_fun as sf


# In[2]:


sf.area_circulo(2)


# In[3]:


sf.PI


# ## Generación de numeros aleatorios

# In[45]:


import random


# In[46]:


numero = random.randint(1, 100) ## Genera numeros aleatorios del 1 al 10
print(numero)


# #### Crear una función que permita llenar una lista de un tamaño definido por el usuario y que pida al usuario cada uno de los datos

# In[49]:


lista=[1,2,3,4,4,4]
len(lista)


# In[50]:


lista[0]


# In[53]:


lista[len(lista)-1]


# In[61]:


lista=[None]*5
lista


# In[63]:


print(lista[3])


# In[64]:


def constru_lista():
    tamano=int(input("Ingrese el tamaño: "))
    lista=[None]*tamano
    
    for i in range(tamano):
        lista[i]=int(input(f"ingrese elemento {i+1}: "))
    return lista
  


# In[65]:


lista=constru_lista()


# In[66]:


lista


# #### Crear un función que llene una lista con números aleatorios entre 1 y 10 y que tenga el  tamaño definido por el usuario

# In[44]:


def lista_aleatoria():
    lon=int(input("Ingrese el tamaño: "))
    lista=[None]*lon
    for i in range(lon):
        lista[i]=random.randint(1, 10)
    return lista


# In[45]:


lista_aleatoria()


# In[ ]:





# ### Parámetros indefinidos

# In[ ]:


def funcion2(*params):
    for i in params:
        print(i)
    return params


# In[ ]:


t=funcion2(2,3,4,4)


# In[ ]:


def listas(**listas):
    print(listas["nombre"])


# In[ ]:


listas(nombre="pedro")


# In[ ]:


type(t)


# In[ ]:


def funcion2(**params):
    for i in params:
        print(f"{i} es {params[i]}")
    return params


# In[ ]:


a=funcion2(i=3,b=4, j="hola")


# In[ ]:


type(a)


# In[64]:


def suma(a,b):
    return a+b
    


# ### Importar desde otro archivo

# In[67]:


from Clase_suma import *


# In[70]:


import Clase_suma as s


# In[73]:


s.suma(5,4)


# In[ ]:


a="ere"
b="123"
b.isdigit()


# In[ ]:


b[2]


# In[64]:


def imprimir():
    """ Esta función se utiliza 
    
    para imprimir DOCSTRING """
    
    print("Función para imprimir")
    print("Otro letrero")


# In[65]:


# imprimir()
help(imprimir)


# In[66]:


print(imprimir.__doc__)


# In[ ]:


def imprimir_2(letrero):
    print(letrero)


# In[ ]:


imprimir_2("Bienvenidos")


# In[ ]:


a=1234
imprimir_2(a)


# In[ ]:


numero=imprimir_2(a)
print(numero)


# In[ ]:


def imprimir_3(letrero):
    print(letrero)
    return letrero


# In[ ]:


numero=imprimir_3(1234)


# In[ ]:


print(numero)


# #### Métodos de búsqueda e inserción en listas

# ## Métodos que se pueden usar con arreglos (o listas)
# 
# |Método||Descripción|
# | --- || --- |
# |append()||Agrega un elemento al final de la lista|
# |clear()||Elimina todos los elementos de la lista|
# |copy()||Devuelve una copia de la lista|
# |count()||Devuelve el número de elementos con el valor especificado|
# |extend()||Agrega los elementos de una lista (o cualquier iterable), al final de la lista actual|
# |index()||Devuelve el índice del primer elemento con el valor especificado|
# |insert()||Agrega un elemento en la posición especificada|
# |pop()||Elimina el elemento en la posición especificada|
# |remove()||Elimina el primer elemento con el valor especificado|
# |reverse()||Invierte el orden de la lista|
# |sort()||Ordena la lista|

# In[13]:


lista=[0,2,3,3,5,334]


# In[ ]:


## Buscar 
3 in lista


# In[ ]:


## Buscar la posición del elemento
lista.index(3)


# In[ ]:


lista2=[10,11,12]
lista[2:2]=lista2


# In[ ]:


lista


# In[ ]:


### Eliminar un elemento por su valor
lista2.remove(11)
lista2


# In[ ]:


### Eliminar un elemento por su índice
lista.pop(1)
lista


# In[18]:


lista.sort(reverse=True)


# In[43]:


lista=[0,2,5,0,4,8,0,8]


# In[32]:


lista=lista[::-1]


# In[33]:


lista.index(min(lista))


# In[46]:


lista


# In[90]:


def intercambio(lista, pos1, pos2):
    temp = arreglo[pos1] #variable temporal
    lista[pos1]=lista[pos2]
    lista[pos2]=temp    

a = [10, 20, 30,10]
intercambio(a, 1, 2)
print(a) 


# In[21]:


max(lista)


# # Ordenamiento y Búsqueda

# In[93]:


def ordenaAscen(arreglo):
    for i in range(0, len(arreglo)-1):
        menor = i
        for j in range(i+1, len(arreglo)):
            if arreglo[j] < arreglo[menor]:
                menor = j
                print(arreglo)
        intercambiar(arreglo, i, menor)

        
arreglo = [30,20,10,80,60]
ordenaAscen(arreglo)
print(arreglo)


# In[107]:


def bubbleSort(arreglo):
    for i in range(0, len(arreglo)-1):
        for j in range(0, (len(arreglo)-1)-i):
            if arreglo[j] > arreglo[j + 1]:
                intercambiar(arreglo, j, j + 1)
                print(arreglo)

arreglo = [2,5,9,4,8,1]
bubbleSort(arreglo)
print(arreglo)

arreglo = [30,20,10,80,60]
bubbleSort(arreglo)
print(arreglo)


# In[101]:


def busLineal(arreglo, d):
    pos = -1
    for x in range(len(arreglo)):
        if(d == arreglo[x]):
            pos = x
            break
#         print(x)
    return pos

arreglo = [10,20,30,40,50]
print(busLineal(arreglo,50))


# In[103]:


def busBinaria(arreglo, d):
    inicio = 0
    fin = len(arreglo)-1
    while inicio <= fin:
        mitad = (inicio + fin) // 2
        if arreglo[mitad] == d:
            return mitad
        if d < arreglo[mitad]:
            fin = mitad - 1
        else:
             inicio = mitad + 1
    return -1

arreglo = [10,20,30,40,50]
print(busBinaria(arreglo,50))


# ### Desempaquetado de parámetros

# In[65]:


numeros=[2,4]
print(suma(*numeros))


# In[66]:


numeros_dicc={"a":2,"b":4}
print(suma(**numeros_dicc))


# ### Construir un archivo con las  funciones de vectores

# ### Introducción a la Programación Orientada a Objetos

# ### Wrappers o empaquetado de funciones

# In[ ]:



def display_arguments(func):
    def display_and_call(*args, **kwargs):      
        args = list(args)
        print('must-have arguments are:')
        for i in args:
            print(i)          
        print('optional arguments are:')
        for kw in kwargs.keys():
            print( kw+'='+str( kwargs[kw] ) )          
        return func(*args, **kwargs)   
    return display_and_call

@display_arguments
def my_add(m1, p1=0):
    output_dict = {}
    output_dict['r1'] = m1+p1
    return output_dict

@display_arguments
def my_deduct(m1, p1=0):
    output_dict = {}
    output_dict['r1'] = m1-p1
    return output_dict


# In[ ]:


def mostrar(func):
    
    def mostrar_llamar(*arg):
        for i in arg:
            print("Entrada: ",i)
        return print("Salida: ",func(*arg))
    
    return mostrar_llamar

@mostrar
def mi_suma(a):
    c=a+a
    return c

@mostrar
def mi_resta(a):
    c=a-2
    return c


# In[ ]:


@mostrar
@mostrar
def my_suma(a):
    c=a+a
    return c


# In[ ]:


my_suma(8)


# In[ ]:


mi_suma(2)


# In[ ]:


mi_resta(5)


# In[ ]:


def decorador(funcion):
    print('Soy el decorador()')
    def wrapper():
        print('Soy el wrapper()')
        return funcion()
    return wrapper

@decorador
def funcion_decorada():
    print('Soy la funcion_decorada()')

funcion_decorada()


# In[92]:


def funcion(c):
    return c*2


# In[93]:


funcion(2.3)


# In[ ]:





# In[ ]:




