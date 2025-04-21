from math import *
import numpy as np

a = 0     # Esto es el limite inferio de la integral
b = 1
n = 5
Vx = (b - a)/n 

suma = 0
x = np.linspace(a,b,n+1)
X = np.linspace(a,b,n+1)

def f(x):
    return x**2

for i in range(n+1):
    x[i] = a + i * Vx

for i in range(n):
    X[i+1] = (x[i]+x[i+1])/2

for i in range(n):   # Este rango es de 0 a 4 [ 0 1 2 3 4 ]
    suma = suma + f(X[i+1]) 

respuesta = Vx * suma

print(respuesta)
