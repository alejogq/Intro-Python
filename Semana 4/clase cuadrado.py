class cuadrado():
    
    def __init__(self):
        
        tamano = int(input("Ingrese el tamaño"))
        color_in = input("Ingrese el color: ")
        
        self.ancho = "* "*tamano
        self.alto = tamano
        self.area = tamano**2
        self.color = color_in
        
    def __str__(self):
        return f"""
    Este objeto tiene ancho: {self.alto}
                       alto: {self.alto}
                       area: {self.area}
                      color: {self.color}
        """
        
    def mostrar(self):
        for i in range(self.alto):
            print("    ",self.ancho)

a= cuadrado()
print(a)
a.mostrar()


