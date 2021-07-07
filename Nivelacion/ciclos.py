
seguir="s"

while (seguir.lower() == "s"):

    kilosPapa = input("Ingrese Kilos de papa (2000 el kilo): ") 
    kilosPapa = kilosPapa.replace("," , ".")
    kilosPapa = float(kilosPapa)
    
    
    kilosTomate = input("Ingrese Kilos de tomate (2500 el kilo): ") 
    kilosTomate = kilosTomate.replace("," , ".")
    kilosTomate = float(kilosTomate)
    
    Total = kilosPapa*2000 + kilosTomate*2500
    Total = int(Total)
      
    print("El costo total es: {:,} ".format(Total))
    
    seguir=input("¿Desea ingresar otros productos? \n (s): Si \n (n): No \n Respuesta: ")

      
    
    
print("Se cerró el programa")











