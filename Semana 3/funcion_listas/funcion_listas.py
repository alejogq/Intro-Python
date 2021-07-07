
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
    
def orgVector(vector):
    temp=vector[1:vector[0]+1]
    vector[1:vector[0]+1]=temp
    return vector


def intercambiar(V, i, j):
    aux = V[i]
    V[i] = V[j]
    V[j] = aux    

    
def ordenaAscen(v):
    for i in range(1, v[0]):
        menor = i
        
        for j in range(i+1, v[0]+1):
            
            if v[j] < v[menor]:
                menor = j
                
        intercambiar(v, i, menor)
        print(v)
    
def burbuja(V):
    for i in range(1, V[0]):
        for j in range(1, V[0] - i + 1):
            if V[j] > V[j+1]:
                intercambiar(V, j, j+1)

# Método de inserción
def insercion(V):
    for i in range(2, V[0]+1):
        d = V[i]
        j = i - 1
        while j > 0 and V[j] > d:
            V[j+1] = V[j]
            j = j - 1
        V[j+1] = d
    

# Verificar si el arreglo esta lleno o no
def esLleno(V, n):
    if V[0] == n:
        return True
    return False



# agrega un dato si tiene espacio
def agregarDato(d, V, n):
    if esLleno(V, n):
        return
    V[0] = V[0] + 1
    V[V[0]] = d
    
def insertarDato(d, i, V, n):
    if esLleno(V, n):
        return    
    for j in range(V[0], i - 1, -1):
        V[j + 1] = V[j]
    V[i] = d
    V[0] = V[0] + 1
    


def mayorDato(V):
    mayor = 1
    for i in range(2, V[0] + 1):
       if V[i] > V[mayor]:
          mayor = i
    return mayor


def buscarDato(V, d):
    i = 1
    while i <= V[0] and V[i] != d:
        i = i + 1
    if i <= V[0]:
        return i
    return -1



def busbin(V, d):
    ## el vector de entrada debe estar ordenado ascendentemente
    inicio = 1
    fin = V[0]
    
    while inicio <= fin:
        mitad = (inicio + fin) // 2
        if V[mitad] == d:
            return mitad
        if d < V[mitad]:
            fin = mitad - 1
        else:
             inicio = mitad + 1
    return -1


def sumaVector(V):
     n = V[0] + 1
     s = 0
     for i in range(1, n):
        s = s + V[i]
     return s


def menorDato(V):
     menor = 1
     for i in range(2, V[0] + 1):
         if V[i] < V[menor]:
              menor = i
     return menor

def borrarDatoEnPosicion(i, V):
    for j in range(i, V[0]):
        V[j] = V[j + 1]
    V[0] = V[0] - 1


def borrarDato(d, V):
     i = buscarDato(d, V)
     if i != -1:
         borrarDatoEnPosicion(i, V)




