from numpy.polynomial.legendre import leggauss 

def gauss():
    x,w = leggauss(3)
    print(x,w)
    y = 0.0
    for i in range(0,2):
        y = y + w[i]*(x[i])**8
    
    return y
    
y = gauss()
print(y)
    

