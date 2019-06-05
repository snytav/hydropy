import numpy as np
import matplotlib.pyplot as plt

# we assume that x contains the interval limits

def w(i,n):
    y = np.zeros(n)
    y[i] = 1.0
    return y

def phi(i,x,x0):
    if i == 0:
       if x0 < x[1]:
          return ((x[1] - x0)/(x[1] - x[0]))
       else:
          return 0.0
    
    if ((x0 > x[i-1]) and (x0 <= x[i])):
       return ((x0 - x[i-1])/(x[i] - x[i-1]))

    if ((x0 >= x[i]) and (x0 < x[i+1])): 
       return ((x[i+1] - x0)/(x[i+1] - x[i]))

    return 0.0

def dphi(i,x,x0):
    if i == 0:
       if x0 < x[1]:
          return - 1.0/(x[1] - x[0])
       else:
          return 0.0

    if ((x0 > x[i-1]) and (x0 <= x[i])):
       return 1.0/(x[i] - x[i-1])

    if ((x0 >= x[i]) and (x0 < x[i+1])):
       return -1.0/(x[i+1] - x[i])

    return 0.0



#n = 10
#x = np.linspace(0,1,n)
#y0 = w(0,n)
#y1 = w(1,n)
#y2 = w(2,n)
#y3 = w(3,n)

#plt.plot(x,y0)
#plt.plot(x,y1)
#plt.plot(x,y2)
#plt.plot(x,y3)
#plt.show()

#x1 = np.linspace(0,1,1000)
#u0 = np.asarray([dphi(0,x,x0) for x0 in x1])

#u1 = np.asarray([dphi(1,x,x0) for x0 in x1])

#u2 = np.asarray([dphi(2,x,x0) for x0 in x1])


#plt.figure
#plt.plot(x1,u0)
#plt.plot(x1,u1)
#plt.plot(x1,u2)
#plt.show()

