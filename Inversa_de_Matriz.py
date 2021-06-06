# Determinar la matriz inversa de dimension 2 x 2

import sys
import numpy as np

#Pedimos datos al usuario para formar la matriz 2 x 2
x1=int(input("Digite el valor de a1,1 ->"))
y1=int(input("Digite el valor de a1,2 ->"))
x2=int(input("Digite el valor de a2,1 ->"))
y2=int(input("Digite el valor de a2,2 ->"))

#Se forma la matriz
a = np.array([[x1,y1],[x2,y2]])

#Muestra la matriz
print (f"La matriz formada es: \n{a}")

#Calcular determinante de la matriz
det = abs((x1 * y2) - (y1 * x2))

#Verificar si el determinante es mayor a 0
if det == 0:
    print(f"Su determinante es: {det}")
    print("La matriz es irregular o singular, no tiene inversa")
    #Si es igual a cero se detiene el programa
    sys.exit()

#Muestra Determinante
print (f"Su determinante es: {det}")

#Adjunta de la matriz
ad1 = (-1)**2 * (y2)
ad2 = (-1)**3 * (x2)
ad3 = (-1)**3 * (y1)
ad4 = (-1)**4 * (x1)

#Forma de la matriz
adj = np.array([[ad1,ad2],[ad3,ad4]])

#Mostramos matriz adjunta
print(f"La matriz adjunta es: \n{adj}")

#Definimos la matriz traspuesta
tras = np.array([[ad1,ad3],[ad2,ad4]])

#Mostramos la matriz traspuesta
print(f"La matriz traspuesta es: \n{tras}")

#Determinamos la matriz inversa
inv = np.array([[ad1/det,ad3/det],[ad2/det,ad4/det]])

#Mostramos la inversa de la matriz
print(f"La inversa de la matriz es: \n{inv}")
