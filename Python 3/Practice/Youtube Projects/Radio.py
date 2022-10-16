from ast import Lambda
from msilib.schema import RadioButton
from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Connor''s frame practice')

TOPPINGS = [
    ('Pepperoni','Pepperoni'),
    ('Cheese', 'Cheese'),
    ('Mushrooms', 'Mushrooms'),
    ('Onion','Onion')
]

pizza = StringVar()
pizza.set('Pepperoni')

for text, mode in TOPPINGS:
    Radiobutton(root, text = text, variable=pizza, value=mode).pack(anchor=W)

def clicked(value):
    myLabel = Label(root, text = value)
    myLabel.pack()

#Radiobutton(root, text = 'option 1', variable=r, value=1, command=Lambda: clicked(r.get())).pack()
#Radiobutton(root, text = 'option 2', variable=r, value=2, command=Lambda: clicked(r.get())).pack()

#myLabel = Label(root, text = pizza.get())
#myLabel.pack()

myButton = Button(root, text='Click Me!', command=lambda: clicked(pizza.get()))
myButton.pack()

root.mainloop()
