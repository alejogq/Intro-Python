import sumar as sf

radio=int(input("Ingrese Radio: "))
altura=int(input("Ingrese altura: "))

volumen = sf.volumen_cilindro(radio, altura)


area=sf.area_circulo(radio)

volumen_2= sf.volumen2(sf.area_circulo(radio),altura)

print(f"Volumen= {volumen} \n Área= {area} \n volumen2= {volumen_2}")




