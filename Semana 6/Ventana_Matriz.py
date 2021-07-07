# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 09:35:38 2021

@author: alejo
"""
from tkinter import ttk
from tkinter import *
from tkinter import colorchooser as ColorChooser
from tkinter import messagebox as MessageBox
from tkinter.ttk import Notebook

class crearVentanas():

    def __init__(self, window):

        self.wind = window
        self.wind.title('VENTANA PRINCIPAL')
        self.wind.geometry('400x200')
        
        ## Creamos dos pestañas para la ventana 
        self.book = Notebook(self.wind)
        self.book.grid(row=0, column=0)#pack(fill='both', expand='yes')
        
        self.f1 = Frame(self.wind, bg="green")
        self.f2 = Frame(self.wind, bg="blue")
        
        self.book.add(self.f1, text='Pestaña 1')
        self.book.add(self.f2, text='Pestaña 2')
        ####
        
        ### Texto de Entrada
        self.cantidad = Entry(self.f1)
        self.cantidad.grid(row=3,column=0)
        
        ### Boton para imprimir la matriz de botones
        self.imprimir=Button(self.f1, 
                             text="imprimir",
                             command= lambda: self.botones(self.f2))
        self.imprimir.grid(row=1,column=0)
        
        ## Creación de los menus
        self.menubar = Menu(self.wind)
        self.wind.config(menu=self.menubar)
        
        self.MenuArchivo = Menu(self.menubar, tearoff=0)
        self.MenuArchivo.add_command(label="Color", command = self.colorN)
        self.MenuArchivo.add_command(label="Salir",command=self.salir)
        
        self.menubar.add_cascade(label="Archivo", menu=self.MenuArchivo)
       
        
    def salir(self):

        resultado = MessageBox.askquestion("Salir", 
            "¿Está seguro que desea salir sin guardar?")
        
        if resultado == "yes":
            print("Salió del programa")
            self.wind.destroy()
        
    
    def colorN(self):
        color = ColorChooser.askcolor(title="Elige un color")
        print(color)
        self.f1['bg'] = color[1]
        
        print(f"""
              Eligió el color: {color[1]} \n
                  Red   = {color[0][0]}
                  Green = {color[0][1]}
                  Blue  = {color[0][2]}
                  
              """)
        
    def mostrar(self):
        self.num = self.cantidad.get()
        

    def botones(self,lugar):
        self.mostrar()
        ## Construimos una matriz de botones
        M=[]
        
        for i in range(1,int(self.num)):
            M.append([])
            for j in range(1,int(self.num)):
                nuevoB=Button(lugar,
                              text = f'{i},{j}').grid(row = i+2,
                                                                column=j)
                
                M[i-1].append(nuevoB)
    
    
    def entradas(self):
        self.mostrar()
        
        M=[]
        
        for i in range(1,int(self.num)+1):
            M.append([])
            for j in range(1,int(self.num)+1):
                nuevoE=Entry(self.wind,text = f'{i},{j}').grid(row = i+2,
                                                                column=j)
                
                M[i-1].append(nuevoE)
    
    
            
if __name__ == '__main__':
    ## Creo un objeto de la clase Tk()
    VPrincipal = Tk()
    
    ## Creo mi objeto de la clase crearVentanas
    application = crearVentanas(VPrincipal)
    
    ## Llamo el método mainloop para mantener la ventana abierta
    VPrincipal.mainloop()