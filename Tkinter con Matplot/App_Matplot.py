# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 22:51:06 2021

@author: alejo
"""

# Mas información para el código de cambio de páginas: 
# http://stackoverflow.com/questions/7546050/switch-between-two-framePagina-in-tkinter
# License:
# http://creativecommons.org/licenses/by-sa/3.0/	


import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np

import tkinter as tk
from tkinter import ttk


FUENTE_APP= ("Verdana", 12)
FUENTE_2= ("Times", 20)

class PaginaPrincipal(tk.Tk):
    """
    Esta clase crea una página principal que hereda de la clase tk.Tk
    """
    
    def __init__(self, *args, **kwargs):
        """
        Se inicializa con los argumentos de la clase padre mas los que nosotros le
        adicionemos
        """
        
        tk.Tk.__init__(self, *args, **kwargs)

        # tk.Tk.iconbitmap(self, default="icono.ico")
        tk.Tk.wm_title(self, "PAGINA PRINCIPAL")
        
        
        contenedor = tk.Frame(self)
        contenedor.pack(side="top", fill="both", expand = True)
        contenedor.grid_rowconfigure(0, weight=1)
        contenedor.grid_columnconfigure(0, weight=1)

        ## se crea un atributo que es un diccionario
        self.framePagina = {}

        for F in (PaginaInicial, PaginaUno, PaginaDos, PaginaTres):

            frame = F(contenedor, self)

            self.framePagina[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(PaginaInicial)

    def show_frame(self, cont):

        frame = self.framePagina[cont]
        frame.tkraise()

        
class PaginaInicial(tk.Frame):

    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self,parent)
        
        label = tk.Label(self, text="Pagina Inicial", font=FUENTE_APP)
        label.pack(pady=10,padx=10)
        
        self.controller=controller
        
        ## Boton que usa un metodo sin el comando lambda:
        button = ttk.Button(self, text="Ir a página 1",
                            command = self.pagina1)
        button.pack()
        
        ## Boton de que usa el comando lambda para definir una función anónima
        button2 = ttk.Button(self, text="Ir a página 2",
                            command=lambda: controller.show_frame(PaginaDos))
        button2.pack()

        button3 = ttk.Button(self, text="Ir al gráfico",
                            command=lambda: controller.show_frame(PaginaTres))
        button3.pack()
        
        aviso=tk.Label(self, text="\n BIENVENIDOS", font=FUENTE_2)
        aviso.pack()
        
    def pagina1(self):
        self.controller.show_frame(PaginaInicial)



class PaginaUno(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Pagina 1", font=FUENTE_APP)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Volver al inicio",
                            command=lambda: controller.show_frame(PaginaInicial))
        button1.pack()

        button2 = ttk.Button(self, text="Página Dos",
                            command=lambda: controller.show_frame(PaginaDos))
        button2.pack()
        
        aviso=tk.Label(self, text="Elementos de la página 1", font=FUENTE_2)
        aviso.pack()


class PaginaDos(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Página 2", font=FUENTE_APP)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Volver al Inicio",
                            command=lambda: controller.show_frame(PaginaInicial))
        button1.pack()

        button2 = ttk.Button(self, text="Página 1",
                            command=lambda: controller.show_frame(PaginaUno))
        button2.pack()
        
        aviso=tk.Label(self, text="Elementos de la página 2", font=FUENTE_2)
        aviso.pack()
        

        x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
        y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
        colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])
        
        sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])
        
        f=Figure(figsize=(5,5), dpi=100)
        a = f.add_subplot(1,1,1)
        a.scatter(x, y, c=colors, cmap='viridis', s=sizes, alpha=0.5)

        lienzo = FigureCanvasTkAgg(f, self)
        lienzo.draw()
        lienzo.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)


class PaginaTres(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Página del Gráfico", font=FUENTE_APP)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Volver al Inicio",
                            command=lambda: controller.show_frame(PaginaInicial))
        button1.pack()
        
        aviso=tk.Label(self, text="GRAFICO DE LA FUNCIÓN", font=FUENTE_2)
        aviso.pack()

        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_subplot(111)
        a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])


        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        ## Si se quiere importar el tool bar.
        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        

app = PaginaPrincipal()
app.mainloop()