"""
Menús y Ventanas Emergentes
"""
from tkinter import ttk
from tkinter import *

from tkinter import colorchooser as ColorChooser
from tkinter import messagebox as MessageBox

def colorN():
    color = ColorChooser.askcolor(title="Elige un color")
    print(f"""
          Eligió el color: {color[1]} \n
              Red   = {color[0][0]}
              Green = {color[0][1]}
              Blue  = {color[0][2]}
              
          """)

def salir():
    resultado = MessageBox.askquestion("Salir", 
        "�Est� seguro que desea salir sin guardar?")
    
    if resultado == "yes":
        print("Salio del programa")
        root.destroy()
        
def alerta():
    MessageBox.showwarning("Alerta", 
        "Presionó el menú alerta")
    
def error():
    MessageBox.showerror("Error", 
    "Ha ocurrido un error inesperado.")
 
def resultado():
    resultado = MessageBox.askokcancel("Salir", 
        "¿Desea hacer algo?")

    if resultado == True:
        print("Confirmó desear hacer algo")

def guardarI(info,salida):
    #entrada=info.get()
    #salida.set(entrada)
    salida.set("Holahola")

root = Tk()
root.geometry('400x200')

etiqueta=Label(root,text="Ingrese texto").grid(row=0,column=0)

## Es necesario separar la definici�n del Entry del .grid, sino
## nos retorna un None dentro de la variable.
Texto_in = Entry(root)
Texto_in.grid(row=0,column=1)


mensaje = StringVar()
mensaje.set("hola")

Etiqueta1 = Label(root)
Etiqueta1.setvar=mensaje
Etiqueta1.grid(row = 2, column=2)


menubar = Menu(root)
root.config(menu=menubar)

MenuArchivo = Menu(menubar, tearoff=0) #tearoff: Elimina un elemento que aparece por defecto
MenuArchivo.add_command(label="Color", command=colorN)
MenuArchivo.add_command(label="Resultado", command=resultado)
MenuArchivo.add_command(label="Error", command=error)
MenuArchivo.add_command(label="Alerta", command=alerta)
MenuArchivo.add_separator()
MenuArchivo.add_command(label="Salir", command=salir)#root.destroy)

MenuEditar = Menu(menubar, tearoff=0)
MenuEditar.add_command(label="Guardar Nombre", command = guardarI(Texto_in,mensaje))
MenuEditar.add_command(label="Copiar")
MenuEditar.add_command(label="Pegar")


Ayuda = Menu(menubar, tearoff=0)
Ayuda.add_command(label="Ayuda")
Ayuda.add_separator()
Ayuda.add_command(label="Acerca de...")

temas = Menu(Ayuda, tearoff=0)
temas.add_command(label="Cortar")
temas.add_command(label="Copiar")
temas.add_command(label="Pegar")
Ayuda.add_cascade(label="Temas",menu=temas)

Complejo = Menu(menubar, tearoff=0)
Complejo.add_command(label="Tarea1")
Complejo.add_checkbutton(label="Seleccion")
Complejo.add_radiobutton(label="Tipo")


menubar.add_cascade(label="Archivo", menu=MenuArchivo)
menubar.add_cascade(label="Editar", menu=MenuEditar)
menubar.add_cascade(label="Ayuda", menu=Ayuda)
menubar.add_cascade(label="Complejo", menu=Complejo)


root.mainloop()



