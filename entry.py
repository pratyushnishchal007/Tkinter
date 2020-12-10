from tkinter import *

top=Tk()
e=Entry(top,width=50,fg="red",bg="cyan")
e.pack()
e.insert(0,"Enter your name")
def myClick():
    myLabel=Label(top,text=e.get())
    myLabel.pack()
myButton=Button(top,text="Enter your name",padx=50,command=myClick,fg="white",bg="black")


myButton.pack()
top.mainloop()