class ColeccionVaciaError(Exception):
    def __init__(self, mensaje):
        self.arg = mensaje


class Cola:
    
    # Propiedad o atributo para
    # alamacenar los elementos de la COLA
    elementos = None
    
    # Constructor para crear una COLA Vacía
    def __init__(self):
        self.elementos = []
        
    # operacion, funcion o metodo para agregar
    # elementos al final de la cola
    def entrar_a_la_cola(self, dato):
        self.elementos.append(dato)
        
    # operacion, funcion o metodo para equitar
    # elementos al inicio o cabeza de la cola
    def salir_de_la_cola(self):
        try:
            item = self.elementos.pop(0)
            return item
        except IndexError:
            raise ColeccionVaciaError("La COLA está Vacía")
            
    # Verificar si la cola esta vacía
    # Devuelve True (verdad) si la cola esta vacila
    # De lo contrario devuelve False (falso)
    def esta_vacia(self):
         return False if self.elementos else True
         #return self.elementos == []
       
    # Devolver el contenido de la cola
    def __str__(self):
        if self.esta_vacia():
            return "COLA Vacia"
        else:
            contenido = "COLA:\n|"
            for i in self.elementos:
                contenido += str(i)+"|"
            return contenido
            
# --- CLASE PARA CREAR OBJETOS QUE SE COMPORTEN COMO UNA PILA -----

class Pila:
    elementos = None

    def __init__(self):
        self.elementos = list()
    
    def colcar_en_la_cima(self, dato):
        self.elementos.append(dato)
        
    def quitar_de_la_cima(self):
        try:
            return self.elementos.pop()
        except IndexError:   
            raise Exception("PILA Vacía")
    
    def esta_vacia(self):
         return False if self.elementos else True
         #return self.elementos == []
    
    def __str__(self):
        if self.esta_vacia():
            return "PILA Vacia"
        else:
            contenido = "PILA:\n──\n"
            for i in range(len(self.elementos)-1, -1, -1):
                contenido += str(self.elementos[i])+"\n──\n"
            return contenido
        
    