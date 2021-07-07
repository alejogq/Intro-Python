# %%
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
        
    
            
# %%
mivector=vector(3)

# %%
mivector.eslleno()

#%%
mivector.agregarDato(6)

#%%
mivector.eliminarDato()

# %%

#### 

class nuevoVec(vector):
    
    def eliminarDato(self):
        posicion = self.V[0]
        self.V[posicion] = 0   
        vector.eliminarDato(self)
        ##super().eliminarDato()

#%%

vector2=nuevoVec(8)

#%%
vector2.agregarDato(4)

#%%

vector2.eliminarDato()












