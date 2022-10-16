
from email import message
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image

root = Tk()
root.title('Connor''s frame practice')

#Different Message boxes: showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

def popup():
   response = messagebox.askyesno('This is my popup', 'Hello World') #First text is title, second is actual message
   Label(root, text = response).pack()
   if response == 1:
    Label(root, text='You Clicked Yes!').pack()
   else:
    Label(root, text='You Clicked No!').pack()

Button(root, text = 'Popup', command = popup).pack()

mainloop()
