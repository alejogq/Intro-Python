#%%
"""
Creamos una ventana pero no la podemos ver, dado que no tenemos un 
ciclo repetitivo que la mantenga en visualización.
"""  
from tkinter import *

ventanaPrincipal = Tk()

#%%
"""
Ya tenemos una ventana que se puede mostrar debido a que utilizamos 
el método mainloop(). Éste método mantiene visible la ventana
"""
from tkinter import *

ventanaPrincipal = Tk()

ventanaPrincipal.mainloop()



#%%
"""
Podemos crear otra ventana a través de:
    Tk():        Es una ventana nueva que no depende de la anterior
    Toplevel():  Es una ventana nueva que depende de una ventana principal
"""
from tkinter import *

ventanaPrincipal = Tk()
ventanaSecundaria = Tk()
ventana3 = Tk()
ventanaSecundaria.mainloop()

## Al ejecutar el mainloop() en la ventana secundaria se abre la ventana
## principal también. Es necesario cerrar todas las ventanas

#%%
from tkinter import *

ventanaPrincipal= Tk()

ventanaSecundaria=Toplevel()
ventana3=Toplevel()
ventana3.mainloop()

## solo debo cerrar una vez
#%%
"""
Tamaños
"""
import tkinter as tk

app = tk.Tk()

app.geometry('400x200')

## para dejar un tamaño fijo de la ventana
app.resizable(0, 0)

# backFrame = tk.Frame(master=app,
#                     width=200,
#                     height=200,
#                     bg='blue')

app.mainloop()

#%%

import tkinter as tk

app = tk.Tk()

app.geometry('400x200')
app.resizable(0, 0)

app2=tk.Tk()
app2.geometry('600x400')

app.mainloop()

#%%
"""
Haremos un botón
"""

import tkinter as ttk

ventanaPrincipal= ttk.Tk()

## creo el botón
miboton = ttk.Button(ventanaPrincipal, text="Hola, mundo!")
miboton2 = ttk.Button(ventanaPrincipal, text="Boton 2!")
##le digo que me ponga el botón

# miboton.place(x=50, y=60, height=400, width=100)

miboton.place(relx=0.4, rely=0.2, relheight=0.4, relwidth=0.2)

miboton2.pack(padx=30,pady=30,ipadx=20, ipady=20)

#miboton2.pack(expand=True, fill = ttk.X)

ventanaPrincipal.mainloop()

# %%
"""
Poner una imagen de fondo
"""
from tkinter import Tk, PhotoImage, Label, Button
# from tkinter import PhotoImage

app = Tk()
app.title("ventana con Imagen")

app.geometry('800x600')

# Lees la imagen:
imagen = PhotoImage(file = "fondo.png")
# Con Label y la opción image, puedes mostrar una imagen en el widget:
fondo = Label(app, image = imagen, text = "Imagen S.O de fondo")
# Con place puedes organizar el widget de la imagen posicionandolo
# donde lo necesites (relwidth y relheight son alto y ancho en píxeles):
fondo.place(x = 0, y = 0, relwidth = 1, relheight = 1)
# Por defecto el fondo es blanco.
fondo.config(bg = "#417c62")

etiqueta = Label(app, text='\n Etiqueta 1 \n')
etiqueta.grid(row=0, column=0)

miboton2 = Button(app, text="Boton 2!").grid(row=3, column=2)



app.mainloop()

#%%
"""
Cambiar el tamaño de los elementos con el tamaño de la ventana
"""

import Tkinter as tk       

app = tk.Tk()                       
area = tk.Frame(app)

## Los elementos se pegan a sus limites: N=norte, S=Sur, E=Este, W=Oeste
area.grid(sticky = tk.N + tk.S + tk.E + tk.W)

app.rowconfigure(0, weight=1)           
app.columnconfigure(0, weight=1) 
       
quitar = tk.Button(app, text='Quitar',
                   command = print("presionó quitar"))

quitar.grid(row=0, column=0,
            sticky = tk.E + tk.S + tk.E + tk.W)  


app.mainloop()  

#%%
"""
Igual al anterior pero con uso de clases

Cambiar el tamaño de los elementos con el tamaño de la ventana
"""

class Application(tk.Frame):     
         
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid(sticky = tk.N + tk.S + tk.E + tk.W)
        self.createWidgets()

    def createWidgets(self):
        top=self.winfo_toplevel() ## pregunta cual es la ventana en el nivel mas alto                
        top.rowconfigure(0, weight=1)            
        top.columnconfigure(0, weight=1) 
        
        self.rowconfigure(0, weight=1)           
        self.columnconfigure(0, weight=1)        
        self.quit = tk.Button(self, text='Quit', 
                              command=self.master.destroy)
        
        self.quit.grid(row=0, column=0,          
            sticky = tk.N + tk.S + tk.E + tk.W)         

app = Application()                       
app.master.title('Sample application')    
app.mainloop()                            

#%%






#%%

"""
Ubicación de elementos
"""

from tkinter import *

ventanaPrincipal = Tk()

# Creando un label o etiqueta
label1 = Label(ventanaPrincipal,
               text = '\n Etiqueta 1 \n')

label1.pack(fill=X)
                                                         
label2 = Label(ventanaPrincipal, 
               text = '\n Etiqueta 2 \n').pack(side=RIGHT)
                                                         
ventanaPrincipal.mainloop()

## solo debo cerrar una vez



#%%
"""
Ubicación de elementos
"""

from tkinter import *

ventanaPrincipal = Tk()

# Creando un label o etiqueta
label1 = Label(ventanaPrincipal, 
                   text = '\n Etiqueta 1 \n').grid(row=0,
                                                    column=3,
                                                    columnspan=5,
                                                    rowspan=5)
                                                         
label2 = Label(ventanaPrincipal, 
                   text = '\n Etiqueta 2 \n').grid(row=6,
                                                    column=3,
                                                    columnspan=5,
                                                    rowspan=5)
                                                         
ventanaPrincipal.mainloop()

## solo debo cerrar una vez

#%%

"""
Añadir imagenes y cambiar fuentes
"""

from tkinter import *
import tkinter.font as tkFont

ventanaPrincipal = Tk()

imagen = PhotoImage(file='fondo.png')
Lbl = Label(width=600, image=imagen).grid(row=30)

# Creando un label o etiqueta
label1 = Label(ventanaPrincipal, 
                   text = '\n Paisaje de Bienvenida 1 \n').grid(row=0,
                                                    column=0,
                                                    columnspan=5)
                                                                
                                                             
                                                         
label2 = Label(ventanaPrincipal, 
                   text = '\n Etiqueta 2 \n').grid(row=6,
                                                    column=3,
                                                    columnspan=5
                                                    )
                                                         
ventanaPrincipal.mainloop()

#%%
"""
CAMBIAR TAMAÑO Y TIPO DE FUENTE
"""

import tkinter as tk
import tkinter.font as tkFont

root = tk.Tk()
root.geometry("400x240")

textExample=tk.Label(root, 
                   text = '\n Paisaje de Bienvenida \n')

textExample2=tk.Label(root, 
                   text = '\n Paisaje de Bienvenida 2 \n')

textExample.pack()
textExample2.pack()

fontExample = tkFont.Font(family="Arial",
                          size=25,
                          weight="bold",
                          slant="italic")

textExample.configure(font=fontExample)

root.mainloop()





#%%
"""
La siguiente estructura con POO es útil para la creación de aplicaciones
dado que permite organizar la creación de los elementos
"""
from tkinter import *

class crearVentanas():

    def __init__(self, window):
        """
        Acá configuramos la estructura de la ventana principal
        y después podemos definir métodos para crear las ventanas secundarias
        """
        pass

"""
Con esta estructura de if, lo que hacemos es preguntar por el archivo
en ejecución y realizamos las 3 operaciones que se indican
"""
if __name__ == '__main__':
    ## Creo un objeto de la clase Tk()
    VPrincipal = Tk()
    
    ## Creo mi objeto de la clase crearVentanas
    application = crearVentanas(VPrincipal)
    
    ## Llamo el método mainloop para mantener la ventana abierta
    VPrincipal.mainloop()

"""
La ventaja que tiene este tipo de estructura es que las ventanas del 
proyecto pueden estar asociadas a archivos independientes y 
en cada clase se define la estructura de las ventanas correspondientes.
"""

#%%
"""
DINÁMICA DE VENTANAS
"""
from tkinter import ttk
from tkinter import *

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
                                        
        self.letrero = StringVar()
        self.letrero.set("inicio")
        
        self.message = Label(self.wind, textvariable=self.letrero).grid(row = 8,
                                                                column=15,
                                                               columnspan = 2)
                                        
        
    def subVentana1(self): 
        """
        Creamos una subventana de la ventana principal
        """
        
        self.letrero.set("Subventana 2 \n fue abierta")
        
        self.ventanita=Toplevel() 
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
    

if __name__ == '__main__':
    ## Creo un objeto de la clase Tk()
    VPrincipal = Tk()
    
    ## Creo mi objeto de la clase crearVentanas
    application = crearVentanas(VPrincipal)
    
    ## Llamo el método mainloop para mantener la ventana abierta
    VPrincipal.mainloop()


#%%

## Ventanas dentro de ventanas
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np

import tkinter as tk
from tkinter import ttk

LARGE_FONT= ("Verdana", 12)

class contenedora(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.iconbitmap(self, default="hola.ico")
        tk.Tk.wm_title(self, "PAGINA CONTENEDORA")
        
        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        ## paginas que se cargarán dentro de la principal
        for F in (StartPage, PageOne):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()
        

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button = ttk.Button(self, text="Visit Page 1",
                            command=lambda: controller.show_frame(PageOne))
        button.pack()
        
        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_subplot(111)
        a.plot([1,2,3,4,5,6,7,8],[5,50,10,30,0,0,3,5])

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button = ttk.Button(self, text="Visit Start",
                            command=lambda: controller.show_frame(StartPage))
        button.pack()

        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_subplot(111)
        a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

app = contenedora()
app.mainloop()

#%%




## Ventanas dentro de ventanas
# import matplotlib
# matplotlib.use("TkAgg")
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
# from matplotlib.figure import Figure
# import matplotlib.pyplot as plt
# import numpy as np

import tkinter as tk
from tkinter import ttk

LARGE_FONT= ("Verdana", 12)

class contenedora(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.iconbitmap(self, default="hola.ico")
        tk.Tk.wm_title(self, "PAGINA CONTENEDORA")
        
        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        ## paginas que se cargarán dentro de la principal
        for F in (StartPage, PageOne):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()
        

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button = ttk.Button(self, text="Visit Page 1",
                            command=lambda: controller.show_frame(PageOne))
        button.pack()
        
        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_subplot(111)
        a.plot([1,2,3,4,5,6,7,8],[5,50,10,30,0,0,3,5])

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button = ttk.Button(self, text="Visit Start",
                            command=lambda: controller.show_frame(StartPage))
        button.pack()

        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_subplot(111)
        a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

app = contenedora()
app.mainloop()

