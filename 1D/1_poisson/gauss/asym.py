import sympy 
import numpy as np
import sys

def phi(i,n):
    #xx = np.linspace(0,1,n)
    x,hx = sympy.symbols('x hx')

    ph = []
    ##print('function num ',i)
    for j in range(0,i):
        ph.append(0.0)
    ##print(ph)
     
    y =  x/hx
    ph.append(y)
    y = 1.0 - x/hx
    ph.append(y)

    for j in range(i+2,n):
#        ##print(j)
        ph.append(0.0)
    ##print(len(ph))
    return ph

# i,j - numbers of basis functions
# num_fe - number of finite element on which the two functions ar being integrated
def get_integration_functions(i,j,num_fe):
    fi = phi(i,n)
    fj = phi(j,n)
    #print('fi ',i,fi)
    #print('fj ',j,fj)

    ic = i
    f1 = fi[num_fe]
    f2 = fj[num_fe]
    #print('integration element ',num_fe)
    #print(f1)
    #print(f2)

    x,hx = sympy.symbols('x hx')

    if type(f1) is float:
       df1 = 0.0
    else: 
       df1 = f1.diff(x)

    if type(f2) is float: 
       df2 = 0.0
    else:
       df2 = f2.diff(x)

    #print('df1 ',i,df1)
    #print('df2 ',j,df2)
 
    return [df1,df2]

def integrate_on_FE(f1,f2,dx):
    x,hx = sympy.symbols('x hx')
    s = sympy.integrate(f1*f2,(x,0,hx))
    #print("integral ",s)
    num = s.subs(hx,dx)
    return num

def integrate_two_functions(i,j,x,ic,prep):
    dx = x[ic] - x[ic-1]
    #print(dx)
    df1,df2 = prep(i,j,ic)
    num = integrate_on_FE(df1,df2,dx)
    return num


def get_stiffness_element(i,j,x,prep):
    if abs(i - j) > 1:
       return 0.0

    n1  = integrate_two_functions(i,j,x,i,prep)
    n2  = integrate_two_functions(i,j,x,j,prep)

    if abs(n1) > 1e-15 and abs(n2) > 1e-15:
       return [n1,n2]

    if abs(n1) < 1e-15:
       return n2
    
    if abs(n2) < 1e-15:
       return n1
 
 
    return 0.0 

n = 23
x = np.linspace(0,1,n)
###print(x)
i = 1
j = 2

num = get_stiffness_element(i,i,x,get_integration_functions)
#print('result ii ',num)
##print('##################################################')
num = get_stiffness_element(j,j,x,get_integration_functions)
#print('result jj ',num)

num = get_stiffness_element(i,j,x,get_integration_functions)
#print('result ij ',num)
##print('##################################################')
num = get_stiffness_element(j,i,x,get_integration_functions)
#print('result ji ',num)

A = np.zeros((n,n))

for i in range(0,n-1):
    for j in range(0,n-1):
        #print(i,j,'#############################################')
        a = get_stiffness_element(i,j,x,get_integration_functions)
        ##print(a)
        ##print(type(a))
        #sys.exit()
        if i == j:
           A[i][i]     += a[0]
           if i < n-2:
              A[i+1][i+1] += a[1] 
        else:   
           #print(i,j,a)  
           A[i][j] += a
        #print(i,j,A[i][j])
       

np.savetxt('Asym.txt',A,fmt='%.2f')
 
