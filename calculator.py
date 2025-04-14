import os
import sys
import tkinter as tk
from tkinter import *
import ttkbootstrap as tktheme
from ttkbootstrap.constants import *
# from ttkbootstrap.widgets import Button


# Determine the correct base directory
if getattr(sys, 'frozen', False):  
    # If the script is running as an EXE, get the temp folder path
    base_path = sys._MEIPASS  
else:
    # If running as a normal Python script, use the script’s directory
    base_path = os.path.dirname(__file__)

# Construct the full path to the icon
icon_path = os.path.join(base_path, "Type 1 icon.ico")
 
root = Tk()

# App Title
root.title("Simple Calculator")
root.config(bg="grey")
root.iconbitmap(icon_path)


# Create a style object
# style = tktheme.Style("superhero")
# info colored button style
# Button(bootstyle="secondary")   

# styled theme
# style = tktheme.Style("superhero")

e = Entry(root, width = 50, borderwidth = 5,font=("Arial", 10), bg="black", fg="white", insertbackground="red", relief= "flat")  # Change either to Label or text component
# e.config(state="disabled")
e.grid(row ="0", column = "0", columnspan = 4, padx = 0, pady= 20, ipady=4)

answer = None 
first_number = e.get()

def button_click(number):
    # e.delete(0, END)
    global current
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

f_num = None
math = None

def button_add():
    try:
        first_number = e.get()
        global f_num
        global math
        math ="addition"
        f_num = float(first_number)
        e.delete(0, END)
    except ValueError:
        if not first_number:
            answer = "Click a Number First!!!"
            e.insert(0, answer)
    
def percentage():
    try:
        global first_number
        first_number = e.get()
        global f_num
        global math
        math ="percentage"
        f_num = float(first_number)
        e.delete(0, END)
    except ValueError:
        if not first_number:
            answer = "Click a Number First!!!"
            e.insert(0, answer)

def button_equal():
    global answer
    global math
    second_number = e.get()
    # e.delete(0, END)
    # e.insert(0,current)
    
    if math == None:
       pass
    
    try:
        if math == "addition":  
            e.delete(0, END)
            answer =  f_num + float(second_number)
            e.insert(0, answer)
            math = None
    except ValueError:
         if not second_number:
                answer = "Click a Second Number!!!"
                e.insert(0, answer)
    try:
        if math == "subtraction":
            e.delete(0, END)
            answer = f_num - float(second_number)
            e.insert(0, answer)
            math = None
    except ValueError:
         if not second_number:
                answer = "Click a Second Number!!!"
                e.insert(0, answer)
                
    try: 
        if math == "multiplication":
            e.delete(0, END)
            answer =  f_num * float(second_number)
            e.insert(0, answer)
            math = None
    except ValueError:
         if not second_number:
                answer = "Click a Second Number!!!"
                e.insert(0, answer) 
                
    try:   
        if math == "division":
            e.delete(0, END)
            answer = round(f_num / float(second_number))
            e.insert(0, answer)
            math = None
    except ValueError:
         if not second_number:
                answer = "Click a Second Number!!!"
                e.insert(0, answer)
                
    try:    
        if math == "percentage":
            e.delete(0, END)
            answer = float(round(  (f_num / 100) , 2 ) ) * float(second_number) 
            e.insert(0, (answer,"%") )
            math = None
    except ValueError:
        if not second_number :
                answer = "Click a Second Number!!!"
                e.insert(0, answer)
        
    if math == "point":
        e.delete(0, END)
        answer = f_num + float(second_number)
        e.insert(0, answer) 
        math = None

def button_subtract():
    try:
        first_number = e.get()
        global f_num
        global math
        math = "subtraction"
        f_num = float(first_number)
        e.delete(0, END)
    except ValueError:
        if not first_number:
            answer = "Click a Number First!!!"
            e.insert(0, answer)
        

def button_multiply():
    try:
        first_number = e.get()
        global f_num
        global math
        math = "multiplication"
        f_num = float(first_number)
        e.delete(0, END)
    except ValueError:
        if not first_number:
            answer = "Click a Number First!!!"
            e.insert(0, answer)

def button_divide():
    try:
        first_number = e.get()
        global f_num
        global math
        math ="division"
        f_num = float(first_number)
        e.delete(0, END)
    except ValueError:
        if not first_number:
            answer = "Click a Number First!!!"
            e.insert(0, answer)
    
def button_point():
    first_number = e.get()
    global f_num
    global math
    math ="point"
    f_num = float(first_number)
    e.delete(0, END)
    
#----------------------------------------------   
# Check if value entered is float , 
# if it is a float number display a float result
# else an integer result
#-----------------------------------------------

# # e.insert(0,)

# Create/Define Buttons
# button_1 = Button(root, text = "1", padding=(20,40), bootstyle="secondary", command = lambda: button_click(1))


button_1 = Button(root, text = "1", padx = 40, pady = 20, background = "black", foreground = "white", command = lambda: button_click(1) )
button_1.config(font=("bold"))

button_2 = Button(root, text = "2", padx = 40, pady = 20, background = "black", foreground = "white", command = lambda: button_click(2))
button_2.config(font=("bold"))


button_3 = Button(root, text = "3", padx = 45, pady = 20,  background = "black", foreground = "white", command = lambda: button_click(3))
button_3.config(font=("bold"))

button_4 = Button(root, text = "4", padx = 40, pady = 20,  background = "black", foreground = "white", command = lambda: button_click(4))
button_4.config(font=("bold"))

button_5 = Button(root, text = "5", padx = 40, pady = 20,  background = "black", foreground = "white", command = lambda: button_click(5))
button_5.config(font=("bold"))

button_6 = Button(root, text = "6", padx = 45, pady = 20,  background = "black", foreground = "white", command = lambda: button_click(6))
button_6.config(font=("bold"))

button_7 = Button(root, text = "7", padx = 40, pady = 20,  background = "black", foreground = "white", command = lambda: button_click(7))
button_7.config(font=("bold"))

button_8 = Button(root, text = "8", padx = 40, pady = 20,  background = "black", foreground = "white", command = lambda: button_click(8))
button_8.config(font=("bold"))

button_9 = Button(root, text = "9", padx = 45, pady = 20,  background = "black", foreground = "white", command = lambda: button_click(9))
button_9.config(font=("bold"))

button_0 = Button(root, text = "0", padx = 40, pady = 28,  background = "black", foreground = "white", command = lambda: button_click(0))
button_0.config(font=("bold"))

button_point = Button(root, text = ".", padx = 40, pady = 28,  background = "black", foreground = "white", command = lambda: button_click("."))
button_point.config(font=("bold"))

button_add = Button(root, text = "+", padx = 40, pady = 20,  background = "black", foreground = "white", command = button_add)
button_add.config(font=("bold"))

button_equal = Button(root, text = "=", padx = 40, pady = 60,  background = "black", foreground = "white", command = button_equal)
button_equal.config(font=("bold"))

button_clear = Button(root, text = "C", padx = 80, pady = 20,  background = "black", foreground = "white", command = button_clear)
button_clear.config(font=("bold"))

button_percentage = Button(root, text = "%", padx = 45, pady = 20,  background = "black", foreground = "white", command = percentage)
button_percentage.config(font=("bold"))

button_subtract = Button(root, text = "-", padx = 40, pady = 20,  background = "black", foreground = "white", command = button_subtract)
button_subtract.config(font=("bold"))

button_multiply = Button(root, text = "*", padx = 40, pady = 20,  background = "black", foreground = "white", command = button_multiply)
button_multiply.config(font=("bold"))

button_divide = Button(root, text = "/", padx = 40, pady = 20,  background = "black", foreground = "white", command = button_divide)
button_divide.config(font=("bold"))

button_1.grid(row = 4, column = 0)
button_2.grid(row = 4, column = 1)
button_3.grid(row = 4, column = 2)

button_4.grid(row = 3, column = 0)
button_5.grid(row = 3, column = 1)
button_6.grid(row = 3, column = 2)

button_7.grid(row = 2, column = 0)
button_8.grid(row = 2, column = 1)
button_9.grid(row = 2, column = 2)
button_multiply.grid(row = 3, column =3, sticky="we")


button_clear.grid(row = 1, column = 0,columnspan=2, sticky="we")
button_add.grid(row = 1, column = 3)
button_percentage.grid(row = 1, column= 2)
button_subtract.grid(row = 2, column =3, sticky="we")

button_equal.grid(row = 4, column = 3 , rowspan = 2, sticky="ns")
button_point.grid(row = 5 ,column= 2, sticky="we")

button_0.grid(row = 5, column = 0,columnspan=2, sticky="we")


# button_divide.grid(row = 1, column =2)


# Put Buttons on Screen
# e.insert(0, "enter your Name: ")
root.resizable(False, False)
root.mainloop()