import numpy as np

#Pedimos datos al usuario para formar la matriz
x1=int(input("Digite el valor de fila 1 columna 1 ->"))
y1=int(input("Digite el valor de fila 1 columna 2 ->"))
z1=int(input("Digite el valor de fila 1 columna 3 ->"))
x2=int(input("Digite el valor de fila 2 columna 1 ->"))
y2=int(input("Digite el valor de fila 2 columna 2 ->"))
z2=int(input("Digite el valor de fila 2 columna 3 ->"))
x3=int(input("Digite el valor de fila 3 columna 1 ->"))
y3=int(input("Digite el valor de fila 3 columna 2 ->"))
z3=int(input("Digite el valor de fila 3 columna 3 ->"))
#Se forma la matriz
a = np.array([[x1,y1,z1],[x2,y2,z2],[x3,y3,z3]])

#Pedimos datos para formar el vector
c1=int(input("Digite el valor para x ->"))
c2=int(input("Digite el valor para y ->"))
c3=int(input("Digite el valor para z ->"))
#Se forma el vector
b = np.array([c1, c2, c3])

#Muestra la matriz
print (f"La matriz formada es: \n{a}")
print (f"EL vector es: \n{b}")

N=len(b)
x=np.zeros(N)

for i in range(N-1):
    b[i]=b[i]/a[i][i]
    a[i]=a[i]/a[i][i]
    for k in range(i+1, N):
        b[k]=b[k]-a[k][i]*b[i]
        a[k]=a[k]-a[k][i]*a[i]

i=N-1
b[i]=b[i]/a[i][i]
a[i]=a[i]/a[i][i]

N=len(a)
for i in reversed(range(N)):
    suma=np.sum(a[i][i+1:]*x[i+1:])
    x[i]=b[i]-suma

print ("La diagonal de la matriz es: \n" ,a, b)
print (x)



