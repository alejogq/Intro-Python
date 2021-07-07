# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 22:14:31 2021

@author: alejo
"""

from tkinter import *

def calcular(textbox):
    a=textbox.get()
    title_label.text="holahola"
    print(a)

main_window=Tk()
# main_window.mainloop()

#Declaramos el marco y sus propiedades
main_frame = Frame(main_window, 
                   bg='#ff0033',
                   height=500, 
                   width=500, 
                   cursor='dot')
            
main_frame.pack() #Lo instanciamos en la interfaz

#Definimos el label y suspropiedades
title_label = Label(main_frame, 
                    text="Hello UI World",
                    font=('Arial',
                          11))  

title_label.pack() #Lo instanciamos en la interfaz
body_label1 = Label(main_frame, text="Bye")
body_label1.pack()

textbox = Entry(main_frame)
textbox.pack()
text_label = Label(main_frame, bg="green")
text_label.pack()

boton = Button(main_frame, text="Hello") #Declaramos el boton y sus propiedades
boton.pack()

boton.command=calcular(textbox)


main_window.mainloop() 