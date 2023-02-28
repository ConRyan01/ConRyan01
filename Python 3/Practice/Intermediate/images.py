from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Connor''s images practice')
root.iconbitmap('C:/Users/ryanc/Pictures/Saved Pictures/Witcher.ico') #gets an icon from a file path to use next to title

my_img = ImageTk.PhotoImage(Image.open('C:/Users/ryanc/Pictures/Saved Pictures/Test.jpg')) #be sure to use / and not \
my_label = Label(image=my_img)
my_label.pack()

button_quit = Button(root, text = 'Exit Program', command=root.quit)
button_quit.pack()

root.mainloop()

