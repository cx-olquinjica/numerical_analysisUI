# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 07:01:46 2020

@author: Aosiwaduo
"""

from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import ImageTk,Image

def NewFile():
    print("New File!")
def OpenFile():
    name = askopenfilename()
    print(name)
def About():
    print("This is a simple example of a menu")
    
root = Tk()
root.title("数值积分典型算法及其应用")

#canvas=Canvas(root,width=300,height=160)
#image=ImageTk.PhotoImage(Image.open("C:\\canvas.png"))
#background_label = Tk.Label(parent, image=background_image)
#background_label.place(x=0, y=0, relwidth=1, relheight=1)
#canvas.create_image(0,0,anchor=NW,image=image)
#canvas.pack()


menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
filemenu1 = Menu(menu)
menu.add_cascade(label="变步长的梯形算法", menu=filemenu)
filemenu.add_command(label="计算", command=NewFile)
filemenu.add_command(label="Open...", command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label="退出", command=root.quit)
menu.add_cascade(label="龙贝格加速算法", menu=filemenu)
menu.add_cascade(label="自适应辛普森算法", menu=filemenu)
menu.add_cascade(label="二重积分计算", menu=filemenu1)
filemenu1.add_command(label="复化梯形公式", command=NewFile)
filemenu1.add_command(label="复化辛普森公式", command=OpenFile)
filemenu1.add_command(label="蒙特卡洛方法", command=OpenFile)

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)

mainloop()