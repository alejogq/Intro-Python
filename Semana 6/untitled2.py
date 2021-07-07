from tkinter import *

# Configuración de la raíz
root = Tk()
root.title("Hola mundo")
root.resizable(1,1)
# root.iconbitmap('hola.ico')

frame = Frame(root, width=480, height=320)
frame.pack(fill='both', expand=1)
frame.config(cursor="star")
frame.config(bg="lightblue")
frame.config(bd=25)
frame.config(relief="sunken")

root.config(cursor="arrow")
root.config(bg="blue")
root.config(bd=15)
root.config(relief="ridge")

# Finalmente bucle de la aplicación
root.mainloop()

#%%

from tkinter import *
from tkinter import colorchooser as ColorChooser
from tkinter import messagebox as MessageBox

from tkinter import colorchooser as ColorChooser

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
        "¿Está seguro que desea salir sin guardar?")
    
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
        # Hacer algo

# Configuración de la raíz
root = Tk()

menubar = Menu(root)
root.config(menu=menubar)

MenuArchivo = Menu(menubar, tearoff=0)#tearoff: Elimina un elemento que aparece por defecto
MenuArchivo.add_command(label="Color", command=colorN)
MenuArchivo.add_command(label="Resultado", command=resultado)
MenuArchivo.add_command(label="Error", command=error)
MenuArchivo.add_command(label="Alerta", command=alerta)
MenuArchivo.add_separator()
MenuArchivo.add_command(label="Salir", command=salir)#root.destroy)

MenuEditar = Menu(menubar, tearoff=0)
MenuEditar.add_command(label="Cortar")
MenuEditar.add_command(label="Copiar")
MenuEditar.add_command(label="Pegar")


Ayuda = Menu(menubar, tearoff=0)
Ayuda.add_command(label="Ayuda")
Ayuda.add_separator()
Ayuda.add_command(label="Acerca de...")

menubar.add_cascade(label="Archivo", menu=MenuArchivo)
menubar.add_cascade(label="Editar", menu=MenuEditar)
menubar.add_cascade(label="Ayuda", menu=Ayuda)

root.mainloop()



