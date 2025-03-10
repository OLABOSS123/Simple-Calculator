from tkinter import *
 
root = Tk()
root.title("Simple Calculator")
e = Entry(root, width = 50, borderwidth = 5,font=("Arial", 10))  # Change either to Label or text component
# e.config(state="disabled")
e.grid(row ="0", column = "0", columnspan = 4, padx = 10, pady= 20, ipady=8)



def button_click(number):
    # e.delete(0, END)
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

f_num = None
math = None

def button_add():
    first_number = e.get()
    global f_num
    global math
    math ="addition"
    f_num = float(first_number)
    e.delete(0, END)
    
def percentage():
    first_number = e.get()
    global f_num
    global math
    math ="percentage"
    f_num = float(first_number)
    e.delete(0, END)

def button_equal():
    global math
    second_number = e.get()
    e.delete(0, END)
    if math == None:
        pass
    if math == "addition":
        e.insert(0, f_num + float(second_number))
        math = None
    if math == "subtraction":
        e.insert(0, f_num - float(second_number))
        math = None
    if math == "multiplication":
        e.insert(0, f_num * float(second_number))
        math = None
    if math == "division":
        e.insert(0, round(f_num / float(second_number)))
        math = None
    if math == "percentage":
        e.insert(0, float(round(  (f_num / 100) , 2 ) ) * float(second_number)   )
        math = None
    if math == "point":
        e.insert(0, f_num + float(second_number))
        math = None

def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_number)
    e.delete(0, END)

def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number)
    e.delete(0, END)

def button_divide():
    first_number = e.get()
    global f_num
    global math
    math ="division"
    f_num = float(first_number)
    e.delete(0, END)
    
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
button_1 = Button(root, text = "1", padx = 40, pady = 20, command = lambda: button_click(1))
button_2 = Button(root, text = "2", padx = 40, pady = 20, command = lambda: button_click(2))
button_3 = Button(root, text = "3", padx = 40, pady = 20, command = lambda: button_click(3))
button_4 = Button(root, text = "4", padx = 40, pady = 20, command = lambda: button_click(4))
button_5 = Button(root, text = "5", padx = 40, pady = 20, command = lambda: button_click(5))
button_6 = Button(root, text = "6", padx = 40, pady = 20, command = lambda: button_click(6))
button_7 = Button(root, text = "7", padx = 40, pady = 20, command = lambda: button_click(7))
button_8 = Button(root, text = "8", padx = 40, pady = 20, command = lambda: button_click(8))
button_9 = Button(root, text = "9", padx = 40, pady = 20, command = lambda: button_click(9))
button_0 = Button(root, text = "0", padx = 80, pady = 20, command = lambda: button_click(0))
button_point = Button(root, text = ".", padx = 40, pady = 20, command = lambda: button_click("."))

button_add = Button(root, text = "+", padx = 40, pady = 20, command = button_add)
button_equal = Button(root, text = "=", padx = 40, pady = 60, command = button_equal)
button_clear = Button(root, text = "C", padx = 80, pady = 20, command = button_clear)

button_percentage = Button(root, text = "%", padx = 40, pady = 20, command = percentage)

button_subtract = Button(root, text = "-", padx = 40, pady = 20, command = button_subtract)
button_multiply = Button(root, text = "*", padx = 40, pady = 20, command = button_multiply)
button_divide = Button(root, text = "/", padx = 40, pady = 20, command = button_divide)

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