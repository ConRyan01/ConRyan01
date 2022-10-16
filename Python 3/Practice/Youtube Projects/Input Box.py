from tkinter import *

root = Tk()

e = Entry(root, width = 50, borderwidth=5)
e.pack() # pack creates the most compact gui window as possible
e.insert(1,'Enter your name:') # insert puts text as default in the entry space

def myClick():
    hello = 'Hello ' + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()

myButton = Button(root, text='Enter Your Name', padx=50, pady=50, command = myClick) # state=DISABLED disables the button, padx & pady change button size
myButton.pack()
root.mainloop()