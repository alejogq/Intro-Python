
class biblioteca():

    def __init__(self,
                 cantidad_in=0,
                 nombre_in="Nueva"
                 ):
        
        self.nombre = nombre_in
        self.cantidad = cantidad_in
        
    def __str__(self):
        return f"{self.nombre}"
    
    def nuevo_libro(self):
        self.libro = input("Ingrese un libro: ")
        
    def metodo(self):
        self.cantidad = input("")
        

micoleccion=biblioteca("Biblioteca central")

micoleccion.metodo()
























