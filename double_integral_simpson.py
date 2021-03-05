# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 14:56:18 2020

@author: Aosiwaduo
"""
import math
from math import sin


  
def givenFunction(x, y):  
   return (math.sin(x+y))/(x+y)

  
# Function to find the double integral value  
def doubleIntegral(h, k, lx, ux, ly, uy):  
  
    # z stores the table  
    # ax[] stores the integral wrt y  
    # for all x points considered  
    z = [[None for i in range(50)] 
               for j in range(50)] 
    ax = [None] * 50
  
    # Calculating the numner of points  
    # in x and y integral  
    nx = round((ux - lx) / h + 1)  
    ny = round((uy - ly) / k + 1) 
  
    # Calculating the values of the table  
    for i in range(0, nx):  
        for j in range(0, ny):  
            z[i][j] = givenFunction(lx + i * h,  
                                    ly + j * k)  
          
    # Calculating the integral value  
    # wrt y at each point for x  
    for i in range(0, nx):  
        ax[i] = 0
        for j in range(0, ny):  
              
            if j == 0 or j == ny - 1:  
                ax[i] += z[i][j]  
            elif j % 2 == 0: 
                ax[i] += 2 * z[i][j]  
            else: 
                ax[i] += 4 * z[i][j]  
          
        ax[i] *= (k / 3)  
      
    answer = 0
  
    # Calculating the final integral  
    # value using the integral  
    # obtained in the above step  
    for i in range(0, nx):  
        if i == 0 or i == nx - 1:  
            answer += ax[i]  
        elif i % 2 == 0: 
            answer += 2 * ax[i]  
        else: 
            answer += 4 * ax[i]  
      
    answer *= (h / 3)  
  
    return answer  
  
# Driver Code  
if __name__ == "__main__": 
  
    # lx and ux are upper and lower limit of x integral  
    # ly and uy are upper and lower limit of y integral  
    # h is the step size for integration wrt x  
    # k is the step size for integration wrt y  
    lx, ux, ly = 1, 4, -2
    uy, h, k = 1, 1, 2
  
    print(round(doubleIntegral(h, k, lx, ux, ly, uy), 6))  
    
    
