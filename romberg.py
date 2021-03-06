import numpy as np
import matplotlib.pyplot as plt
import math
from math import sin
from math import sqrt
# def f1(x):
#    f1 = x**4.0
#    return f1;

# def f2(x):
#    f2 = np.exp(-x*x)
#    return f2;

# def f3(x):
#    tau   = 1.0e-8
#    f3    = np.where(np.abs(x)<tau,1.0,np.sin(x)/x)
#    return f3;

# def f1(x):
  
#    return  sqrt(1+1*2*math.sin(2*x)*math.sin(2*x))

# trapezoidal rule
def trapezoid(f, a, b, n):
        calcular =(0.5)*( f(a) + f(b) )
        h = (b-a)/n
        for i in range(1, n):
            calcular += f(a + i*h)
        return h*calcular

# romberg method
def romberg(f,a,b,eps,nmax):
# f     ... function to be integrated
# [a,b] ... integration interval
# eps   ... desired accuracy
# nmax  ... maximal order of Romberg method
    Q         = np.zeros((nmax,nmax),float)
    converged = 0
    for i in range(0,nmax):
        N      = 2**i
        Q[i,0] = trapezoid(f,a,b,N)
        for k in range(0,i):
            n        = k + 2
            Q[i,k+1] = 1.0/(4**(n-1)-1)*(4**(n-1)*Q[i,k] - Q[i-1,k])
        if (i > 0):
            if (abs(Q[i,k+1] - Q[i,k]) < eps):
               converged = 1
               break
    print (Q[i,k+1],N,converged)  
    return Q[i,k+1],N,converged

# main program
# a  = -1;b = 1  # integration interval [a,b]
# romberg(f1,a,b,0.0000001,50)
# romberg(f2,a,b,1.0e-12,10)
# a  = 0.0;b = 20.0*np.pi  # integration interval [a,b]
# romberg(f3,a,b,1.0e-12,10)
# romberg(sin,0,1,1.0e-12,10)


"""Trapezoid Rule:
    This code approximates the integral of f(x) over [a, b]
    by adding up the areas of n trapezoids.
    
def trapezoid1(f, a, b, n):
        integral = 0
        h = (b-a)/n
        for i in range(n):
            integral += 0.5*h*(f(a + i*h) + f(a + (i+1)*h))
        return integral
        
        here comes a much more efficient code:
            
   def trapezoid2(f, a, b, n):
        integral = 0.5*( f(a) + f(b) )
        h = (b-a)/n
        for i in range(1, n):
            integral += f(a + i*h)
        return h*integral
        
        
        ###### Monte Carlo Integration for Double Integral
        
        import numpy as np
        
        def monte_carlo(f, a, b, c, d, n):
            
            sum = 0.
            for i in range(n):
            sum += f(a+(b-a)*np.random.rand(),
                     c+(d-c)*np.random.rand())*(b-a)*(d-c)
            return sum/n
"""
