

#Clase estrella

class Estrella():
    
    lugar = "Espacio" #Se crea un atributo para la clase
    
    def __init__(self,
                 color_in = "Blanca",
                 edad_in = 0,
                 constelacion_in="nula"
                 ):
        
        self.color = color_in  ## Se crea un atributo para el objeto
        self.edad = edad_in
        self.constelacion = constelacion_in


#crear un objeto de la clase estrella
miestrella  = Estrella("Azul",10000)
miestrella2 = Estrella("Verde")
miestrella3 = Estrella("Amarillo")

miestrella4 = Estrella("Roja")
miestrella4.lugar = "Otra dimensión"

miestrella5 = Estrella()

miestrella6 = Estrella(color_in="azul", edad_in=1000, constelacion_in="Sagitario")











