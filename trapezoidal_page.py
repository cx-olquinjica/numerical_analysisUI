# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 19:53:52 2020

@author: Aosiwaduo
"""
from math import sin,cos, log  
from tkinter import*
import tkinter as tk
from trapezoidal_rule import trapezoid2

def getInput():
    
    a = int(txtLargefries.get())
    print(a)
    b = int(txtupperl.get())
    print(b)
    c= int( txtn_steps.get())
    print(c)
    global d
    d = trapezoid2(sin, a, b,c)
    print(d)
    show_result()

    global params
    params = [a,b,c]
    
def show_result():
    import tkinter.messagebox as tkmb
    
    info_message = d
    # info message box
    tkmb.showinfo("积分结果", info_message)



def trap():
    
    roo1 = tk.Tk()
    roo1.geometry("600x220+0+0")
    roo1.title("变步长的梯形算法")
    lblLargefries = tk.Label(roo1, font=( 'aria' ,16, 'bold' ),text="lower limit",fg="steel blue",bd=10,anchor='w')
    lblLargefries.grid(row=2,column=0)
    global txtLargefries, txtupperl,txtn_steps
    txtLargefries = tk.Entry(roo1,font=('ariel' ,16,'bold'), bd=6,insertwidth=4,bg="powder blue" ,justify='right')
    txtLargefries.grid(row=2,column=1)
            
    upperl = tk.Label(roo1, font=( 'aria' ,16, 'bold' ),text="upper limit",fg="steel blue",bd=10,anchor='w')
    upperl.grid(row=3,column=0)
    txtupperl = tk.Entry(roo1,font=('ariel' ,16,'bold'), bd=6,insertwidth=4,bg="powder blue" ,justify='right')
    txtupperl.grid(row=3,column=1)
    
    
    n_steps = tk.Label(roo1, font=( 'aria' ,16, 'bold' ),text="nº of steps",fg="steel blue",bd=10,anchor='w')
    n_steps.grid(row=4,column=0)
    txtn_steps = tk.Entry(roo1,font=('ariel' ,16,'bold'), bd=6,insertwidth=4,bg="powder blue" ,justify='right')
    txtn_steps.grid(row=4,column=1)
    
    
    btn= Button(roo1, padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text = "计算", bg="powder blue",
       command = getInput).grid(row = 5, column = 1)
    
    
    
    roo1.mainloop()
