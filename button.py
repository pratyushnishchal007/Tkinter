from tkinter import *

top=Tk()

def myClick():
    myLabel=Label(top,text="You clicked the button")
    myLabel.pack()
myButton=Button(top,text="click me!",padx=50,command=myClick,fg="white",bg="black")
#You can also change the color by the help of 'fg' and 'bg'
#myButton=Button(top,text="click me!",state=DISABLED,padx=50,pady=10)
#state = DISABLED means the button will be disabled
#we can also change the size of button by the help of: padx and pady

myButton.pack()
top.mainloop()