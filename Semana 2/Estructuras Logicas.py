#!/usr/bin/env python
# coding: utf-8

# # Estructuras Lógicas

# ## Estructura if
# #### Si entonces

# In[2]:


a=0
b=3

if a==3 and b==0:
    print("a y b son los buscados")
else:
    print("a y b No concuerdan")
    


# In[7]:


a=input("ingrese un número: ")
b=input("ingrese otro número: ")

if a>b:
    print(f"El numero {a} es mayor que el número {b} ")
elif b>a:
    print(f"El numero {b} es mayor que el número {a}")
elif a==b:
    print(f"El numero {a} es igual al número {b}")


# ### Ciclo for

# In[10]:


for i in range(1,10):
    print(f"Ejecución del ciclo {i}")


# In[12]:


for i in range(1,10):
    print(f"Ejecución del ciclo {i}")
    if i==7:
        break


# ## Ciclo while

# In[14]:


i=0
while i<10:
    print(f"Ejecución del ciclo {i}")
    i=i+1


# In[ ]:


i=0
while i<10:
    print(f"Ejecución del ciclo {i}")
    i=i+1
    if i==6:
        break


# ## Iteración sobre estructuras de datos

# In[17]:


tienda={"camas"     : 10,
        "cojines"   : 40,
        "almohadas" : 30,
        "marcas"    : ["pluma ok", "pulman","comodos"]
  }


# In[31]:


## Llaves
tienda.keys()


# In[32]:


## Datos
tienda.values()


# In[18]:


for i in tienda:
    print(i)


# In[22]:


for i in tienda:
    print(tienda[i])


# In[27]:


for i in tienda:
    if type(tienda[i])!= 'int':
        print(tienda[i])
    else:
        print(i)


# In[28]:


lista=[1,2,3,4,5,6,7,8]

for i in lista[2:5]:
    print(lista[i])


# In[30]:


tupla=(1,2,3,4,5,6,7,8)

for i in tupla[2:5]:
    print(tupla[i])


# In[ ]:




