import tkinter as ttk


class CrearVentanas:
    # connection dir property
    db_name = 'database.db'

    def __init__(self, window):
        # Initializations 
        self.wind = window
        self.wind.title("Ventana 1")
        
        # Creating a Frame Container 
        frame = ttk.LabelFrame(self.wind, 
                           text = '\n Frame para datos \n')
        
        frame.grid(row = 0, column = 0, 
                   columnspan = 3, pady = 20)
        
        ttk.Button(frame,
                    text = 'Nueva ventana',
                    command = self.nuevaVentana).grid(row = 3,
                                                      column=1,
                                                    columnspan = 2)#,
                                                    #sticky = W + E)
                                                    
    def nuevaVentana(self):
        
        
        # self.edit_wind = ttk.Toplevel()
        
        # Acá creamos una nueva ventana igual a la principal
        wind2=ttk.Toplevel()
        self.edit_wind = CrearVentanas(wind2)
        
        self.edit_wind.title = 'Ventana Nueva'
        
        ttk.Button(self.edit_wind,
            text = 'Nueva ventana',
            command = self.nuevaVentana).grid(row = 3,
                                            columnspan = 2,
                                            sticky = ttk.W + ttk.E)
        
        self.edit_wind.mainloop()
        
        
                                                    
if __name__ == '__main__':
    ## Creo un objeto de la clase Tk()
    VPrincipal = ttk.Tk()
    
    ## Creo mi objeto de la clase crear ventanas
    application = CrearVentanas(VPrincipal)
    
    ## Llamo el método mainloop para mantener la ventana abierta
    VPrincipal.mainloop()
    
    
    
    
    
    
    
    