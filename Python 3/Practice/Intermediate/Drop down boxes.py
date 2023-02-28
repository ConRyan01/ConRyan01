from cProfile import label
from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Connor''s new window')
root.iconbitmap('C:/Py Images/Witcher.ico')
root.geometry('400x400')

def show():
    mylabel = Label(root, text=clicked.get() ).pack()

options = {
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday'
}

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options) #must use * when passing a list
drop.pack()

myButton = Button(root, text='show selection', command = show).pack()

mainloop()

