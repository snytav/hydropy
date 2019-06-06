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

def get_integration_functions(i,j):
    fi = phi(i,n)
    fj = phi(j,n)
    print(fi)
    print(fj)

    ic = i
    f1 = fi[ic]
    f2 = fj[ic]
    x,hx = sympy.symbols('x hx')

    df1 = f1.diff(x)
    df2 = f2.diff(x)
    print(df1)
    print(df2)
 
    return [df1,df2]

def integrate_on_FE(f1,f2,dx):
    x,hx = sympy.symbols('x hx')
    s = sympy.integrate(df1*df2,(x,0,hx))
    print("integral ",s)
    num = s.subs(hx,dx)
    return num


n = 10

i = 2
j = 3

df1,df2 = get_integration_functions(i,j)

num = integrate_on_FE(df1,df2,0.25)
print(num)
