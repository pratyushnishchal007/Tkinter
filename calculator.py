from tkinter import *

top=Tk()
top.title("Calculator")
e=Entry(top,width=40,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def button_click(numbers):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(numbers))
def button_clear():
    e.delete(0,END)

def button_add():
    first_num=e.get()
    global f_num
    global math
    math="addition"
    f_num=int(first_num)
    e.delete(0,END)
def button_equal():
    second_num=e.get()
    e.delete(0,END)
    if math=="addition":
        e.insert(0,f_num+int(second_num))
    if math == "substraction":
        e.insert(0, f_num - int(second_num))
    if math == "multiplication":
        e.insert(0, f_num * int(second_num))
    if math == "division":
        e.insert(0, f_num / int(second_num))
def button_substract():
    first_num=e.get()
    global f_num
    global math
    math="substraction"
    f_num=int(first_num)
    e.delete(0,END)

def button_multiply():
    first_num=e.get()
    global f_num
    global math
    math="multiplication"
    f_num=int(first_num)
    e.delete(0,END)

def button_divide():
    first_num=e.get()
    global f_num
    global math
    math="division"
    f_num=int(first_num)
    e.delete(0,END)

# Defining the buttons
Button_1=Button(top,text="7",padx=35,pady=20,command=lambda:button_click(7))
Button_2=Button(top,text="8",padx=35,pady=20,command=lambda:button_click(8))
Button_3=Button(top,text="9",padx=35,pady=20,command=lambda:button_click(9))
Button_4=Button(top,text="4",padx=35,pady=20,command=lambda:button_click(4))
Button_5=Button(top,text="5",padx=35,pady=20,command=lambda:button_click(5))
Button_6=Button(top,text="6",padx=35,pady=20,command=lambda:button_click(6))
Button_7=Button(top,text="1",padx=35,pady=20,command=lambda:button_click(1))
Button_8=Button(top,text="2",padx=35,pady=20,command=lambda:button_click(2))
Button_9=Button(top,text="3",padx=35,pady=20,command=lambda:button_click(3))
Button_0=Button(top,text="0",padx=35,pady=20,command=lambda:button_click(0))
ButtonAdd=Button(top,text="+",padx=33,pady=20,command=button_add)
ButtonSubstract=Button(top,text="-",padx=35,pady=20,command=button_substract)
ButtonMultiply=Button(top,text="*",padx=38,pady=20,command=button_multiply)
ButtonDivide=Button(top,text="/",padx=38,pady=20,command=button_divide)
ButtonEqual=Button(top,text="=",padx=82,pady=20,command=button_equal)
ButtonClear=Button(top,text="Clear",padx=73,pady=20,command=button_clear)

# Put the buttons on the screen
Button_1.grid(row=1,column=0)
Button_2.grid(row=1,column=1)
Button_3.grid(row=1,column=2)
Button_4.grid(row=2,column=0)
Button_5.grid(row=2,column=1)
Button_6.grid(row=2,column=2)
Button_7.grid(row=3,column=0)
Button_8.grid(row=3,column=1)
Button_9.grid(row=3,column=2)
Button_0.grid(row=4,column=0)
ButtonAdd.grid(row=5,column=0)
ButtonSubstract.grid(row=6,column=0)
ButtonMultiply.grid(row=6,column=1)
ButtonDivide.grid(row=6,column=2)
ButtonEqual.grid(row=5,column=1,columnspan=2)
ButtonClear.grid(row=4,column=1,columnspan=2)
top.mainloop()