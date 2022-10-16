from cProfile import label
from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Connor''s new window')
root.iconbitmap('C:/Py Images/Witcher.ico')
root.geometry('400x400')

vertical = Scale(root, from_=0, to=200)
vertical.pack()

horizontal = Scale(root, from_=0, to=200, orient=HORIZONTAL)
horizontal.pack()

def slide():
    my_label = Label(root, text=horizontal.get()).pack()

my_btn = Button(root, text = 'click me', command=slide).pack()

mainloop()

