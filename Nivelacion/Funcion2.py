
def ingreso_datos(producto,precio):
    temporal=input(f"Ingrese Kilos de {producto} ({precio} el kilo): ") 
    temporal = temporal.replace("," , ".")
    temporal = float(temporal)
    
    return temporal


def validacion(seguir):
    
    while (seguir.lower() != "s") or (seguir.lower() != "n") :
        print("ERROR EN DATO, INGRESE UN DATO VALIDO")
        seguir=input("¿Desea ingresar otros productos? \n (s): Si \n (n): No \n Respuesta: ")
        
        if ((seguir.lower() == "s")):  
            break
        elif((seguir.lower() == "n")):
            break
        
    return seguir


seguir="s"

pTomate = 2800
pPapa = 1500

while (seguir.lower() == "s"):

    kilosPapa = ingreso_datos("Papa",pPapa)
    kilosTomate = ingreso_datos("Tomate",pTomate)

    Total = kilosPapa*pPapa + kilosTomate*pTomate
    Total = int(Total)
      
    print("El costo total es: {:,} ".format(Total))
    
    seguir=input("¿Desea ingresar otros productos? \n (s): Si \n (n): No \n Respuesta: ")
    
    seguir = validacion(seguir)
  
    
print("Se cerró el programa")
