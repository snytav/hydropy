import numpy
from basis_functions import phi,dphi

x = numpy.linspace(0,1,10)
y = phi(0,x,0.02)
print(y)

y = dphi(0,x,0.02)
print(y)


