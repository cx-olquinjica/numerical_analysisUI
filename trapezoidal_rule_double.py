# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 14:49:33 2020

@author: Aosiwaduo
"""
import numpy as np
import math
from math import sin
from sympy.abc import x
import sympy

def trapezoidal_double(f, a, b, c, d, nx, ny):
    hx = (b - a)/float(nx)
    hy = (d - c)/float(ny)
    I = 0.25*(f(a, c) + f(a, d) + f(b, c) + f(b, d))
    Ix = 0
    for i in range(1, nx):
        xi = a + i*hx
        Ix += f(xi, c) + f(xi, d)
    I += 0.5*Ix
    Iy = 0
    for j in range(1, ny):
        yj = c + j*hy
        Iy += f(a, yj) + f(b, yj)
    I += 0.5*Iy
    Ixy = 0
    for i in range(1, nx):
        for j in range(1, ny):
            xi = a + i*hx
            yj = c + j*hy
            Ixy += f(xi, yj)
    I += Ixy
    I *= hx*hy
    return I

#print(trapezoidal_double(sin, 0, 2, 2, 3, 5, 3))

def test_trapezoidal_double():
    ##Test that a linear function is integrated exactly
    def f(x, y):
        return (sympy.sin(x+y))/(x+y)

    a = 0;  b = 4;  c = -2;  d = 1

    x, y = sympy.symbols('x  y')
    I_expected = sympy.integrate(f(x, y), (x, a, b), (y, c, d))
    # Test three cases: nx < ny, nx = ny, nx > ny
    for nx, ny in (1, 2), (1, 1), (3, 2):
        I_computed = trapezoidal_double(f, a, b, c, d, nx, ny)
        tol = 0.001
   
        #print I_expected, I_computed
        assert abs(I_computed - I_expected) < tol
        
        print(I_expected)
        print(I_computed)
      
        

if __name__ == '__main__':
    test_trapezoidal_double() 