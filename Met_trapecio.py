from math import *
import numpy as np

a = 0
b = 1
n = 5
Vx = (b - a)/n 

suma = 0
x = np.linspace(a,b,n+1)

def f(x):
    return x**2      

for i in range(n+1):
    x[i] = a + i*Vx

for i in range(n-1):
    suma = suma + 2*f(x[i+1]) 

suma = suma + f(x[0]) + f(x[n])

respuesta = Vx/2 * suma

print(respuesta)
