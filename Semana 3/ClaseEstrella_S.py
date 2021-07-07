
import random as rd
#Clase estrella

class Estrella():
    """
    Para usar esta clase haga lo siguiente:
        
    """
    lugar = "Espacio" #Se crea un atributo para la clase
    
    def __init__(self,
                 color = None,
                 edad = None,
                 constelacion=None
                 ):

        self.color = color  ## Se crea un atributo para el objeto
        self.edad = edad
        self.constelacion = constelacion

    def __str__(self):
        return f""" Es un objeto de la Clase Estrella:
                       Color={self.color}
                       Edad= {self.edad}
                       Constelacion= {self.constelacion}
                """              
    def edad_aleatoria(self):
        self.edad = rd.randint(1,10000)
        print(f"edad = {self.edad}")
        
    
    
    
#crear un objeto de la clase estrella: Instanciación, o instanciar.
miestrella  = Estrella("Azul",10000)

miestrella2 = Estrella("Verde")
miestrella3 = Estrella("Amarillo")

miestrella4 = Estrella("Roja")

miestrella4.lugar = "Otra dimensión"

miestrella5 = Estrella()

miestrella6 = Estrella(color="azul", edad=1000, constelacion="Sagitario")



miestrellas=[miestrella, miestrella2, miestrella3]

catalogo={"Betelgesue":miestrella, "Orion": miestrella2}

for i in miestrellas:
    i.lugar="otra dimension"
    print(i)











