# solve the 1D poisson equation x'' = 1 by finite element method
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import scipy.linalg as lina
import numpy.random as rnd
from scipy import integrate
#from basis_functions import phi,dphi

def generate_mesh_random(n):
    x = rnd.random(n)
    x = np.sort(x)
    x = np.append(0.0,x)
    x = np.append(x,1.0)
    return x

def generate_mesh_uniform(n):
    x = np.linspace(0,1,n)
    return x

def compute_element_sizes(x):
    dx = x[1:] - x[:-1]
    return dx 
   
def stiffness_matrix(dx):
    A  = np.diag(1.0/dx[:-1],0) + np.diag(1.0/dx[1:],0)
    A  = A - np.diag(1.0/dx[1:-1],1)
    A  = A - np.diag(1.0/dx[1:-1],-1)
    return A

#def dphi_i_dphi_j(i
#def gauss(A,x):
    


def load_vector(dx):
    b = (dx[:-1] + dx[1:])/2.0
    return b

n = 23
x = generate_mesh_uniform(n)

dx = compute_element_sizes(x)

A  = stiffness_matrix(dx)
np.savetxt('A.txt',A,fmt='%.2f')


b = load_vector(dx)

c = lina.solve(A,b)

#plt.plot(x[1:-1],c)
#plt.show()
print(dx[2])
xx = np.linspace(0,1,1000)

plt.plot(xx,0.5*xx*(1-xx))
plt.plot(x[1:-1],c)
plt.show()
