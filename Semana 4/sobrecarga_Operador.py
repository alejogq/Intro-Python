#%%

class inventario():
    
    def __init__(self,tamano):
        self.V=[0]*tamano
        
    def __add__(self,a):
        
        sum=[0]*(len(b))
        for i in range(len(self.V)):
            sum[i]=self.V[i]+b.V[i]
           
        suma=inventario(len(b))
        suma.V=sum
        
        return suma
    
    def sumar(self, b):
        sum=[0]*(len(b))
        for i in range(len(self.V)):
            sum[i]=self.V[i]+b.V[i]
           
        suma=inventario(len(b))
        suma.V=sum
        
        return suma
    
    def __len__(self):
        l=self.V
        return len(l)
#%%
a= inventario(5)
print(len(a))


#%%
a= inventario(5)
b= inventario(5)

#%%
b.V=[1,2,3,4,5]
a.V=[5,4,3,2,1]

#%%
c = a + b
d=a.sumar(b)

#%%
print(c.V)

#%%








