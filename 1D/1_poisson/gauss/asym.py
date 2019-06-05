import sympy
import numpy as np

def phi(i,n):
    #xx = np.linspace(0,1,n)
    x,hx = sympy.symbols('x hx')

    ph = []
    for j in range(0,i-1):
        ph.append(0.0)
     
    y = 1 - x/hx
    ph.append(y)
    y = x/hx
    ph.append(y)

    for j in range(i+2,n):
        print(j)
        ph.append(0.0)

    return ph 
n = 10

f = phi(2,n)
print(f)
