from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Connor''s new window')
root.iconbitmap('C:/Py Images/Witcher.ico')

def open():
    global my_img
    top = Toplevel()
    my_img = ImageTk.PhotoImage(Image.open('C:/Py Images/Test.jpg'))
    my_label = Label(top, image = my_img).pack()
    btn2 = Button(top, text = 'close window', command = top.destroy).pack()

btn = Button(root, text = 'Open second window', command=open).pack()

mainloop()

