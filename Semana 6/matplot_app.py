#%%
"""
Ejemplo de programa
"""
from tkinter import *
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np



class crearVentanas():

    def __init__(self, window):
        """
        Acá configuramos la estructura de la ventana principal
        
        """
        self.wind = window
        self.wind.title('VENTANA PRINCIPAL')
        self.ven2=False
        
        # Añadimos un botón para abrir una subventana
        Button(self.wind,
            text = 'Subventana',
            command = self.subVentana1).grid(row = 3,
                                             column=1,
                                             columnspan = 2)
                                             
        # Añadimos un botón para abrir una ventana nueva
        Button(self.wind,
            text = 'VENTANA 2',
            command = self.subVentana2).grid(row = 3,
                                             column=15,
                                             columnspan = 2)
        
        # Añadimos un botón para abrir una ventana nueva Independiente
        Button(self.wind,
            text = 'Independiente',
            command = self.subVentana3).grid(row = 3,
                                             column=30,
                                             columnspan = 2) 
                                             
        # BOTON PARA CERRAR
        Button(self.wind,
            text = 'CERRAR',
            command = self.cerrar).grid(row = 5,
                                        column=15,
                                        columnspan = 2)
        # BOTON PARA GRAFICAR
        Button(self.wind,
            text = 'GRAFICAR',
            command = self.graficar).grid(row = 8,
                                        column=15,
                                        columnspan = 2)
        
        # Frame para los gráficos                                  
        self.frame = LabelFrame(self.wind, 
                           text = '\n Frame GRAFICAS \n').grid(row = 8,
                                                                column=20,
                                                                columnspan = 2)
                                        
    def subVentana1(self): 
        """
        Creamos una subventana de la ventana principal
        """
        self.ventanita=Toplevel() 
        
        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_subplot(111)
        a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])
        
        canvas = FigureCanvasTkAgg(f, self.ventanita)
        canvas.draw()
        canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)

        self.ventanita.title = 'Ventana Nueva'
        self.ventanita.mainloop()
    
    
    def subVentana2(self):
        """
        Creamos una ventana con la misma structura de la ventana principal
        que depende de la ventana principal
        
        """
        self.ven2=True
        self.ventana2=Tk()
        self.subVentana=crearVentanas(self.ventana2)
        self.ventana2.title = 'Ventana Nueva 1'
        self.ventana2.mainloop()
        
        
    def subVentana3(self):
        """
        Creamos una ventana con la misma structura de la ventana principal
        que NO depende de la ventana principal
        
        """
        ventana3=Tk()
        VentanaNueva=crearVentanas(ventana3)
        ventana3.title = 'Ventana Nueva 3'
        ventana3.mainloop()
        
    def cerrar(self):
        ## Cierra las ventanas dependientes.
        if self.ven2==True:
            self.subVentana.cerrar()
            self.wind.destroy()
        else:
            self.wind.destroy()
            
            
    def graficar(self):

        matplotlib.rcParams.update({'font.size': 12})
        ax = plt.gca()
        
        ax2 = ax.twinx()
        
        for i in range(10):
            ax.bar(i, np.random.randint(1000))
        
        plt.ylabel('Datos')
        plt.savefig("Ejemplo.jpg", bbox_inches='tight')
    
    

if __name__ == '__main__':
    ## Creo un objeto de la clase Tk()
    VPrincipal = Tk()
    
    ## Creo mi objeto de la clase crearVentanas
    application = crearVentanas(VPrincipal)
    
    ## Llamo el método mainloop para mantener la ventana abierta
    VPrincipal.mainloop()






