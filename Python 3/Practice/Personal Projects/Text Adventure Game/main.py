from curses.ascii import isalpha
from msilib import CreateRecord
from tkinter import *
from turtle import width
from PIL import ImageTk,Image
import sqlite3
from mainGame import game

root = Tk()
root.title('Adventure Game')
root.geometry('300x400')

# create a database or connect one
conn = sqlite3.connect('character_save.db')

#create cursor - a cursor fetches data between program and DB
c = conn.cursor()

#create table - only need to execute this block once to create a db file

# c.execute('''CREATE TABLE addresses ( 
#      name text,
#      gender text,
#      str integer,
#      dex integer,
#      con integer,
#      int integer)''')

def characterCreator():
    global creator
    creator = Tk()
    creator.title('Character Creator')
    creator.geometry('300x400')

def nameInput():
    return

def loadCharacter():
    return

#playerName = input('Enter your character\'s name: ')
#if len(playerName) > 15 or len(playerName) <= 0:
#    print('name must be greater that 0 characters and less than 15 characters')

#elif playerName.isalpha() == True:

#else:
#    print('invalid input: name must be letters only and no spaces')

mainMenu_title = Label(root, text = 'Main Menu',font='Castellar 30 bold underline')
mainMenu_title.grid(row=0,column=1,columnspan=3)

createPlayer_btn = Button(root, text='Create Character', command=characterCreator, width=30, height=3)
createPlayer_btn.grid(row=3,column=1,padx=30,pady=20,columnspan=3,rowspan=2)

play_btn = Button(root, text='Play',command=game, width=30, height=3)
play_btn.grid(row=1,column=1,padx=30,pady=20,columnspan=3,rowspan=2)

load_btn = Button(root, text = 'Load Character', command = loadCharacter, width=30, height=3)
load_btn.grid(row=5,column=1,padx=30,pady=20,columnspan=3,rowspan=2)

#commit changes
conn.commit()

mainloop()
