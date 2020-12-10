from tkinter import *
top=Tk()
#creating a Label Widget
myLabel1=Label(top,text="Hello world")
myLabel2=Label(top,text="My name is Pratyush")
#Shoving it onto the screen
myLabel1.grid(row=0,column=0)
myLabel2.grid(row=1,column=0)

top.mainloop()
