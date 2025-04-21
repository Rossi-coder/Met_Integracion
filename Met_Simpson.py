from math import *
import numpy as np

a = 0
b = 1
n = 4             
Vx = (b - a)/n 

suma = 0

x = np.linspace(a,b,n+1)

def f(x):
    return x**2
 
for i in range(1,n):
    x[i] = a + i*Vx

    if (i%2 == 0):
        suma = suma + 2*f(x[i])
    else:
        suma = suma + 4*f(x[i])

suma = suma + f(x[0]) + f(x[n])

respuesta = suma*(1/3)*Vx

print(respuesta)
