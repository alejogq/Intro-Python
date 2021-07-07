

contador = 10
cont_2=0

print('Empezando')

while contador > 0 :
    
    contador = contador - 2
    print(f"Contador = {contador}")  # parte del ciclo while
    
    while cont_2 < 10:
        
        cont_2 +=1
        print(f"cont_2 = {cont_2}")
        
        if cont_2 == 5:
            cont_2 +=1
            continue
        print("no hubo continue")

print()         # no hace parte del ciclo
print('Hecho')


palabra="ola"
while palabra!="hola":
    print("entro al ciclo")
    palabra=input("ingrese la palabra ")


