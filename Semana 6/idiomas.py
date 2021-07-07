import Tkinter as Tk
root = Tk.Tk()
root.title('Program')
menuButton = Tk.Button(root, text='Menu')
menuButton.grid(row=0, column=0)
root.mainloop()

def change_language(lang):
    if lang == 'English':
        root.title('Program')
        menuButton.config(text='Menu')
    elif lang == 'Spanish':
        root.title('Programa')
        menuButton.config(text='Menú')

english = ['Program', 'Menu']
spanish = ['Programa', 'Menú']

def change_language_2(lang):
    root.title(lang[0])
    menuButton.config(text=lang[1])
