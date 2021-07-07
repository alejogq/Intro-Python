import random

PI = 3.1416

def area_circulo(radio):
    global PI
    area = PI*(radio**2)
    PI=3.14159
    return area

def volumen_cilindro(radio, altura):
    volumen = area_circulo(radio)*altura
    return volumen
    
def volumen2(area,altura):
    volumen=area*altura
    return volumen

def constru_lista():
    tamano=int(input("Ingrese el tamaño: "))
    lista=[None]*tamano
    
    for i in range(tamano):
        lista[i]=int(input(f"ingrese elemento {i+1}: "))
    return lista

def lista_aleatoria(num1, num2):
    
    lon=int(input("Ingrese el tamaño: "))
    lista=[None]*lon
    for i in range(lon):
        lista[i]=random.randint(num1, num2)
    return lista














