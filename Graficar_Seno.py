#Diseñe un codigo que encuentre el sen(pi/3) a travez del desarrollo de Taylor
#truncar cuando n=50

#Cargamos las librerias
import math
import numpy as np

#Aplicar valores dados en el ejercicio
x = np.sin(np.pi/3)
n = 50

#Aplicar un acumulador e iniciarlo
pol = 0.0

#Encabezado
print("\n\n{:^2} {:^16} {:^22}".format("Termino", "k", "Sen (pi/3)"))

#Definimos el ciclo de suma de la serie de taylor para n = 50
for k in range (n):
    pol = pol + (-1)**k * x**(2*k+1) / math.factorial((2*k+1))
    print("\n\n{:^2d} {:^25d} {:^15.10f}".format(k+1, k, pol))