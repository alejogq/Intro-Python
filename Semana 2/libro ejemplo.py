# -*- coding: utf-8 -*-
libro={}

while True:
    print("Elementos disponibles\n",
               "Capitulo [c] \n",
               "Glosario [G] ")
    
    tipo=input(" Ingrese el elemento a asignar: ")
    if tipo.lower() == "c":
        tipo_name=input("ingrese el nombre del capitulo: ")
        elemento=input("Elementos disponibles para capitulo \n Paginas[p] \n Titulos\n Ingrese el elemento a asignar: ")
        
        if elemento.lower() == "p":
            # elemento_name=input("ingrese el nombre del elemento: ")
            dato=input(f"Ingrese los datos correspondientes al {elemento}: ")
            # libro={tipo_name:{elemento:dato}}
            libro[tipo_name]={"Páginas":dato}
    
    pregunta=input("¿Desea agregar otro elemento? ")
    
    if pregunta=="s":
        continue
    else:
        break
