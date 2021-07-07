
"""
Crear una función que reciba una lista y la imprima elemento por 
elemento

"""

def imprimir_listas(accesorios):
    for i in accesorios:
        print(i)
        
def imprimir_inv_listas(accesorios):
    accesorios=accesorios[::-1]
    for i in accesorios:
        print(i)
        
def organizar(numeros):
    
    numeros.sort()
    
    return numeros
    
def eliminar(lista,elemento):
    lista.pop(elemento)


def buscar(lista, elemento):
    
    if elemento in lista:
        posicion=lista.index(elemento)
        return posicion
    else:
        print("No está en la lista")
        return 

def elim_pos(lista,posi,posf):

    lista[posi:posf+1]=[]
    
    return lista
    

def insertar(lista, elemento, pos):
    lista[pos:pos]=[elemento]
    
    return lista

def insertar_lista(lista1, lista2,  pos):
    lista1[pos:pos]=lista2
    return lista1

    
def organizar_inv(numeros):
    lista=organizar(numeros)[::-1]
    return lista


"""
Realizar una función que me busque un dato dentro de una lista
y me diga cuantas veces está dentro de la lista
"""

lista=["pan","arepa","croissant","oblea"]

def buscar_cant(lista,elemento):
    
    contador=0
    for objeto in  lista:
        if objeto == elemento:
            contador+=1
    
    if contador==0:
        print(f"El elemento {elemento} no se encuentra en la lista")
        
        return
    else:
        print(f"El numero de elementos {elemento} es: {contador}")
        return contador
    
    print("termino el proceso")        

"""
vector=[numelemento, 1,2,2,2,2,None, None]

"""    

def buscar_cant_vec(vector,elemento):
    
    posiciones=[]
    contador=0
    
    for posicion in range(1,vector[0]+1):
        
        if vector[posicion]==elemento:
            contador+=1
            posiciones.append(posicion)
        
    if contador==0:
        print(f"El elemento {elemento} no se encuentra en la lista")
        return
    else:
        print(f"El numero de elementos {elemento} es: {contador}")
        return contador, posiciones
    
    print("termino el proceso")



def crear_vector(tamano):
    vector=[0]*(tamano+1)
    return vector
    





            
    
    


    






