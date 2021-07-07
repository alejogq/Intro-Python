

class vector():
    
    def __init__(self, tamano):
        self.V = [0]*(tamano+1)
        self.nt = tamano
    
    def eslleno(self):
        if self.V[0] == self.nt :
            print("El vector está lleno")
            return True
        
        else:
            return False
        
    def agregarDato(self,d):
        if self.eslleno() :
            return
        else:
            posicion=self.V[0]+1
            self.V[posicion] = d
            
            self.V[0] = self.V[0]+1
            
    def eliminarDato(self):
        self.V[0]= self.V[0]-1
