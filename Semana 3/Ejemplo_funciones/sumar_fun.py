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