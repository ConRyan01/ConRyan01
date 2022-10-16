from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text='look! I clicked a button!')
    myLabel.pack()

myButton = Button(root, text='Click Me!', padx=50, pady=50, command = myClick, bg='blue') # state=DISABLED disables the button, padx & pady change button size
myButton.pack()
root.mainloop()