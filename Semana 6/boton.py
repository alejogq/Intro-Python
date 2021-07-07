from tkinter import *



ventana = Tk()


entry = Entry(ventana, width=10)

entry.insert(0, "Hola mundo!")

entry.place(x=50, y=50)

# button = Button(ventana,
#                 text="Obtener texto",
#                 command=lambda: print(entry.get()))

A=0
button = Button(ventana,
                text="Obtener texto",
                command= lambda: input(entry.get()))


button.place(x=50, y=100)

ventana.mainloop() 



 