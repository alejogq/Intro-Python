import tkinter as tk
import tkinter.font as tkFont

root = tk.Tk()
root.geometry("400x240")

textExample=tk.Label(root, 
                   text = '\n Paisaje de Bienvenida \n')

textExample2=tk.Label(root, 
                   text = '\n Paisaje de Bienvenida 2 \n')

textExample.pack(side="right")
textExample2.pack()

fontExample = tkFont.Font(family="Arial",
                          size=25,
                          weight="bold",
                          slant="italic")

textExample.configure(font = fontExample)

root.mainloop()

