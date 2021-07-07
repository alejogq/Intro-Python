import sumar_fun 

radio=int(input("Ingrese Radio: "))
altura=int(input("Ingrese altura: "))

volumen = volumen_cilindro(radio, altura)


area=area_circulo(radio)

volumen_2=volumen2(area_circulo(radio),altura)

print(f"Volumen= {volumen} \n Área= {area} \n volumen2= {volumen_2}")



