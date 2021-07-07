
class cuadrado():
    
    def __init__(self,tamano):
        self.ancho="* "*tamano
        self.alto=tamano
        
    def __str__(self):
        return f"""Este objeto tiene tamaño {self.alto}"""
        
    def mostrar(self):
        print("\n")
        for i in range(self.alto):
            print("    "+self.ancho)

a=cuadrado(10)

a.mostrar()