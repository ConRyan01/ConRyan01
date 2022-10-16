from tkinter import *

root = Tk()

myLabel1 = Label(root, text = "Hello World!") #creating a label widget
mylabel2 = Label(root, text = 'My name is Connor Ryan')

myLabel1.grid(row=0, column=0) #shoving it onto the screen
mylabel2.grid(row=1, column=0)

root.mainloop()