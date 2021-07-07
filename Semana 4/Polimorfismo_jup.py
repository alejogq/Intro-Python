
class Estrella():
    
    def __init__(self, color, tamano):
        self.color=color
        self.tamano=tamano
    
    def titilar(self):
        print(f"**** Soy una estrella titilando con color {self.color} ****")      

class Bombilla():
    
    def __init__(self, color, tamano):
        self.color=color
        self.tamano=tamano
    
    def titilar(self):
        print(f" ---- BOMBILLO titilando con color {self.color} -----")

mibombilla = Bombilla("Amarillo",10)
miestrella = Estrella("Azul", 5)
lista = [mibombilla, miestrella]

for i in lista:
    i.titilar()



#  ### POLIMORFISMO POR HERENCIA

# In[49]:


class marrones(Estrella):
    
    def __init__(self):
#        super().__init__("Marron",5)
        Estrella.__init__(self,"Marron",5)
        self.edad = 500

    def titilar(self):
        print("//// Las Estrellas Marrones no Titilamos ////")
        
        


# In[51]:


estrellaMarron=marrones()


# In[46]:


estrellaMarron.titilar()


# In[10]:


estrellaMarron.edad


# In[41]:


class abuelo():
    def __init__(self, nombre):
        self.nombre=nombre
        print("Constructor ejecutado")
        
    def trabajo(self):
        self.trabajo="Obrero"

class padre(abuelo):
    pass

class hijo(padre):

    def oficio(self):
        self.trabajo="constructor"


# In[42]:


a=hijo("Pedro")


# In[36]:


a.nombre


# In[28]:


a.oficio()


# In[29]:


a.trabajo


# In[ ]:




