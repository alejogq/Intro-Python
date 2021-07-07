from matriz import *


A= Matriz(3, 3)
A.construyeMatriz()

B= Matriz(3, 3)
B.construyeMatriz()

print(A.mat)
A.imprimeMatrizPorFilas("Impresion de la matriz")

print(f"""
      Filas:    {A.numeroFilas()}
      Columnas: {A.numerocolumnas()}    
      
      Suma triangular inferior:
          {A.sumaTriangularInferior()}
      
      """
      )


A.imprimeMatrizPorFilas("Matriz por filas")
          
A.imprimeMatrizPorColumnas("Matriz por columnas")

T=A.traspuesta()
T.imprimeMatrizPorFilas("Matriz traspuesta")

print("\nProducto Diagonal:\n", 
      A.productoDiagonalPrincipal())

print("\nSuma Filas:\n", 
      A.sumarFilas().V)

print("\nSuma Filas:\n", A.sumarColumnas().V)

print("\nSuma triangular Superior:\n",
      A.sumaTriangularSuperior())

print("\nSuma triangular Inferior:\n", 
      A.sumaTriangularInferior())

print("\nSuma triangular estrictamente superior:\n",
      A.sumaTriangularEstrictamenteSuperior())

print("\nSuma triangular estrictamente inferior:\n",
      A.sumaTriangularEstrictamenteInferior())


C=A+B
D=A*B

C.imprimeMatrizPorFilas("Resultado de la suma: ")
D.imprimeMatrizPorFilas("Resultado de la multiplicación: ")








