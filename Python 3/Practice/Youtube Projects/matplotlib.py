from tkinter import *
from PIL import ImageTk,Image
import numpy as np
import matplotlib.pyplot as plt

#main purpose of this is to learn how to connecto to API
root = Tk()
root.title("Connor's Weather App")
root.iconbitmap('C:/Py Images/Witcher.ico')
root.geometry('600x100')

def graph():
    house_prices = np.random.normal(200000, 25000, 5000)
    plt.hist(house_prices, 50)
    plt.show()

root.mainloop()

