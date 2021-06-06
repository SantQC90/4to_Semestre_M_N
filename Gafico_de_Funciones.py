#Garficar las siguientes funciones
#f(x) = x^2 - x + 1
#g(x) = 2 / (x-1)

#Importar librerias
import numpy as np
import matplotlib.pyplot as plt

#Damos valores al eje de las x
x = np.linspace(-3,4,50)

#Escribimos la funcion f(x) = x^2 - x + 1
y1 = x**2-x+1

#Escribimos la funcion g(x) = 2 / (x-1)
y2 = 2/(x-1)

#Graficamos las funciones
plt.plot(x, y1, label = "f(x)")
plt.plot(x, y2, label = "g(x)")

#Editamos la grafica
plt.xlabel("EJE X")
plt.ylabel("EJE Y")
plt.title("GRAFICA DE DOS FUNCIONES")
plt.grid()
plt.legend()
plt.show()
