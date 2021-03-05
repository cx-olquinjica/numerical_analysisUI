# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 06:12:26 2020

@author: Aosiwaduo
"""

import numpy as np

def inverse_power_method(A, tolerance=1e-10, max_iterations=10000):
    
    n = A.shape[0]
    x = np.ones(n)
    I = np.eye(n)
    
    q = np.dot(x, np.dot(A, x)) / np.dot(x, x)
    
    p = __find_p(x)
    
    error = 1
    
    x = x / x[p]
    
    for _ in range(max_iterations):
        
        if error < tolerance:
            break
            
        y = np.linalg.solve(A - q * I, x)       
        μ = y[p]      
        p = __find_p(y)     
        error = np.linalg.norm(x - y / y[p],  np.inf)
        x = y / y[p]
        μ = 1. / μ + q 
    return (μ, x)

"""Power Method começa aqui."""

def __find_p(x):
    return np.argwhere(np.isclose(np.abs(x), np.linalg.norm(x, np.inf))).min()

def __iterate(A, x, p):
    
    y = np.dot(A, x)       
    μ = y[p]      
    p = __find_p(y)     
    error = np.linalg.norm(x - y / y[p],  np.inf)
    x = y / y[p]
    
    return (error, p, μ, x) 

def power_method(A, tolerance=1e-10, max_iterations=10000):
    
    n = A.shape[0]
    x = np.ones(n)
    
    p = __find_p(x)
    
    error = 1
    
    x = x / x[p]
    
    for _ in range(max_iterations):
        
        if error < tolerance:
            break
            
        error, p, μ, x = __iterate(A, x, p)
        
    
    return (μ, x)


