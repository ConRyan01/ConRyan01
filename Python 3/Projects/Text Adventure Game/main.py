
from tkinter import *
import sqlite3
from mainGame import game
import customtkinter
import random
from tkinter import messagebox

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.title("Adventure Game")
root.geometry("300x300")

creator = None

# create a database or connect one
conn = sqlite3.connect("character_file.db")

# create cursor - a cursor fetches data between program and DB
c = conn.cursor()

# create table - only need to execute this block once to create a db file
tableCheck = c.execute('''SELECT name FROM sqlite_master WHERE type='table' AND name='character_save' ''').fetchall()
if tableCheck==[]:
    c.execute('''CREATE TABLE character_save (
        name text,
        gender text,
        class text,
        strength integer,
        dexterity integer,
        intelligence integer,
        constitution integer)''')
    print('tabel created')

roll_stats_btn = None
rollStats_counter = 3
rollStats_counter_label = None

#stat label initialization
stren_value_label=0
dexty_value_label=0
intel_value_label=0
const_value_label=0

attribute_points=5
attribute_points_label=None

#incremental button value initialization
stren_inc_up_btn=None
stren_inc_down_btn=None
dexty_inc_up_btn=None
dexty_inc_down_btn=None
intel_inc_up_btn=None
intel_inc_down_btn=None
const_inc_up_btn=None
const_inc_down_btn=None

def loadCharacter():
    return

# rolls stats for button in characterCreator func
def rollStats(stren,intel,dexty,const,counter,attr):
    global roll_stats_btn
    global rollStats_counter
    global attribute_points_label
    global attribute_points
    stren.configure(text = random.randrange(1, 7) + random.randrange(1, 7) + random.randrange(1, 7))
    intel.configure(text = random.randrange(1, 7) + random.randrange(1, 7) + random.randrange(1, 7))
    dexty.configure(text = random.randrange(1, 7) + random.randrange(1, 7) + random.randrange(1, 7))
    const.configure(text = random.randrange(1, 7) + random.randrange(1, 7) + random.randrange(1, 7))

    # prevents user from cheesing code to reroll stat more than 3 times. Change rollStats_counter initial value to increase number of rolls
    rollStats_counter = rollStats_counter - 1
    rollStats_counter_label.configure(text=rollStats_counter)
    if rollStats_counter <= 0:
        roll_stats_btn.configure(state=DISABLED)
    
    stren_inc_up_btn.configure(state=NORMAL)
    dexty_inc_up_btn.configure(state=NORMAL)
    intel_inc_up_btn.configure(state=NORMAL)
    const_inc_up_btn.configure(state=NORMAL)

    attribute_points = 5
    attribute_points_label.configure(text=attribute_points)

def incrementStatsUp(increment,attr):
    global stren_value_label,dexty_value_label,intel_value_label,const_value_label,attribute_points,attribute_points_label
    global stren_inc_up_btn, stren_inc_down_btn,dexty_inc_up_btn,dexty_inc_down_btn,intel_inc_up_btn,intel_inc_down_btn,const_inc_up_btn,const_inc_down_btn
    if increment==stren_value_label:
       stren_value_label.configure(text= int(stren_value_label._text) + 1)
    if increment==dexty_value_label:
       dexty_value_label.configure(text= int(dexty_value_label._text) + 1)
    if increment==intel_value_label:
       intel_value_label.configure(text= int(intel_value_label._text) + 1)
    if increment==const_value_label:
       const_value_label.configure(text= int(const_value_label._text) + 1)

    attribute_points=attribute_points-1
    attribute_points_label.configure(text=attribute_points)

    if int(attribute_points_label._text) == 0:
        stren_inc_up_btn.configure(state=DISABLED)
        dexty_inc_up_btn.configure(state=DISABLED)
        intel_inc_up_btn.configure(state=DISABLED)
        const_inc_up_btn.configure(state=DISABLED)
    elif int(attribute_points_label._text) < 5 and int(attribute_points_label._text)>0:
        stren_inc_up_btn.configure(state=NORMAL)
        dexty_inc_up_btn.configure(state=NORMAL)
        intel_inc_up_btn.configure(state=NORMAL)
        const_inc_up_btn.configure(state=NORMAL)
        # stren_inc_down_btn.configure(state=NORMAL)
        # dexty_inc_down_btn.configure(state=NORMAL)
        # intel_inc_down_btn.configure(state=NORMAL)
        # const_inc_down_btn.configure(state=NORMAL)

    # sets a stat value cap at 20
    if int(stren_value_label._text) == 20:
        stren_inc_up_btn.configure(state=DISABLED)
    if int(dexty_value_label._text) == 20:
        dexty_inc_up_btn.configure(state=DISABLED)
    if int(intel_value_label._text) == 20:
        intel_inc_up_btn.configure(state=DISABLED)
    if int(const_value_label._text) == 20:
        const_inc_up_btn.configure(state=DISABLED)

def submitCharacter():
    conn = sqlite3.connect('character_file.db')
    global rollStats_counter

    #create cursor - a cursor fetches data between program and DB
    c = conn.cursor()

    #ensures there are no blank entries into the database
    if len(name_box.get()) <= 2 or len(gender_seg.get()) == 0 or len(class_seg.get()) == 0: 
        messagebox.showerror('Invalid Input','Please make sure an option is selected for each section and that your character name is at least 3 and less than 20 characters long')

    #ensures that character name is not numbers or special characters
    elif name_box.get().isalpha() == FALSE:
        messagebox.showerror('Invalid Name','Character name must be letters only')

    else:    
        c.execute('INSERT INTO character_save VALUES(:name,:gender,:class,:strength,:dexterity,:intelligence,:constitution)',
        
            {
            'name':name_box.get(),
            'gender':gender_seg.get(),
            'class':class_seg.get(),
            'strength':int(stren_value_label.cget('text')),
            'dexterity':int(dexty_value_label.cget('text')),
            'intelligence':int(intel_value_label.cget('text')),
            'constitution':int(const_value_label.cget('text'))
            })
    
        rollStats_counter=3

        #commit changes
        conn.commit()

        #close connection
        conn.close()

        creator.destroy()

# def decrementStatsDown(decrement,attr):
#     global stren_value_label,dexty_value_label,intel_value_label,const_value_label,attribute_points,attribute_points_label
#     global stren_inc_up_btn, stren_inc_down_btn,dexty_inc_up_btn,dexty_inc_down_btn,intel_inc_up_btn,intel_inc_down_btn,const_inc_up_btn,const_inc_down_btn
#     if decrement==stren_value_label:
#        stren_value_label.configure(text= int(stren_value_label._text) - 1)
#     if decrement==dexty_value_label:
#        dexty_value_label.configure(text= int(dexty_value_label._text) - 1)
#     if decrement==intel_value_label:
#        intel_value_label.configure(text= int(intel_value_label._text) - 1)
#     if decrement==const_value_label:
#        const_value_label.configure(text= int(const_value_label._text) - 1)
    
#     attribute_points=attribute_points+1
#     attribute_points_label.configure(text=attribute_points)

#     if int(attribute_points_label._text)==5:
#         stren_inc_down_btn.configure(state=DISABLED)
#         dexty_inc_down_btn.configure(state=DISABLED)
#         intel_inc_down_btn.configure(state=DISABLED)
#         const_inc_down_btn.configure(state=DISABLED)
#     elif int(attribute_points_label._text) < 5 and int(attribute_points_label._text)>0:
#         stren_inc_up_btn.configure(state=NORMAL)
#         dexty_inc_up_btn.configure(state=NORMAL)
#         intel_inc_up_btn.configure(state=NORMAL)
#         const_inc_up_btn.configure(state=NORMAL)
#         stren_inc_down_btn.configure(state=NORMAL)
#         dexty_inc_down_btn.configure(state=NORMAL)
#         intel_inc_down_btn.configure(state=NORMAL)
#         const_inc_down_btn.configure(state=NORMAL)

def characterCreator():
    global creator
    global rollStats_counter,attribute_points,attribute_points_label,name_box,gender_seg,class_seg
    global roll_stats_btn,rollStats_counter_label
    global stren_value_label,dexty_value_label,intel_value_label,const_value_label
    global stren_inc_up_btn,stren_inc_down_btn,dexty_inc_up_btn,dexty_inc_down_btn,intel_inc_up_btn,intel_inc_down_btn,const_inc_up_btn,const_inc_down_btn

    creator = customtkinter.CTkToplevel(root)
    creator.title("Character Creator")
    creator.geometry("800x700")
    creator.grab_set()

    # create the character creator entry fields: Name, Gender, Class
    name_box_label = customtkinter.CTkLabel(master=creator, text="Character Name:", font=("papyrus", 18, "bold"))
    name_box_label.grid(row=1, column=1, padx=30, pady=20)
    name_box = customtkinter.CTkEntry(master=creator, placeholder_text="Type Your Character's Name")
    name_box.grid(row=1, column=2, padx=30, pady=20, ipadx=40,columnspan=2)

    gender_label = customtkinter.CTkLabel(master=creator, text="Character Gender:", font=("papyrus", 18, "bold"))
    gender_label.grid(row=2, column=1, padx=30, pady=20)
    gender_seg = customtkinter.CTkSegmentedButton(master=creator, values=["Female", "Male", "Other"])
    gender_seg.grid(row=2, column=2, padx=30, pady=20,columnspan=2)

    class_label = customtkinter.CTkLabel(master=creator, text="Class:", font=("papyrus", 18, "bold"))
    class_label.grid(row=3, column=1, padx=30, pady=20)
    class_seg = customtkinter.CTkSegmentedButton(master=creator, values=["Warrior", "Rogue", "Mage"])
    class_seg.grid(row=3, column=2, padx=30, pady=20,columnspan=2)

    # stats initialization
    stat_stren_label = customtkinter.CTkLabel(master=creator, text="Strength:", font=("papyrus", 18, "bold"))
    stat_stren_label.grid(row=4, column=1, padx=30, pady=5)
    stren_value_label = customtkinter.CTkLabel(master=creator, text="0", font=("papyrus", 18, "bold"))
    stren_value_label.grid(row=4, column=2, padx=30, pady=5,columnspan=2)
    stren_inc_up_btn = customtkinter.CTkButton(master=creator, text = '+',command=lambda:incrementStatsUp(stren_value_label,attribute_points), font=('papyrus',18,'bold'),width=10)
    stren_inc_up_btn.grid(row=4,column=2,padx=1,sticky=E,columnspan=2)
    # stren_inc_down_btn = customtkinter.CTkButton(master=creator, text = '-',command=lambda:decrementStatsDown(stren_value_label,attribute_points), font=('papyrus',18,'bold'),width=10)
    # stren_inc_down_btn.grid(row=4,column=2,padx=1,sticky=E,columnspan=2)

    stat_dexty_label = customtkinter.CTkLabel(master=creator, text="Dexterity:", font=("papyrus", 18, "bold"))
    stat_dexty_label.grid(row=6, column=1, padx=30, pady=5)
    dexty_value_label = customtkinter.CTkLabel(master=creator, text="0", font=("papyrus", 18, "bold"))
    dexty_value_label.grid(row=6, column=2, padx=30, pady=5,columnspan=2)
    dexty_inc_up_btn = customtkinter.CTkButton(master=creator, text = '+',command=lambda:incrementStatsUp(dexty_value_label,attribute_points), font=('papyrus',18,'bold'),width=10)
    dexty_inc_up_btn.grid(row=6,column=2,padx=1,sticky=E,columnspan=2)
    # dexty_inc_down_btn = customtkinter.CTkButton(master=creator, text = '-',command=lambda:decrementStatsDown(dexty_value_label,attribute_points), font=('papyrus',18,'bold'),width=10)
    # dexty_inc_down_btn.grid(row=6,column=2,padx=1,sticky=E,columnspan=2)

    stat_intel_label = customtkinter.CTkLabel(master=creator, text="Intelligence:", font=("papyrus", 18, "bold"))
    stat_intel_label.grid(row=8, column=1, padx=30, pady=5)
    intel_value_label = customtkinter.CTkLabel(master=creator, text="0", font=("papyrus", 18, "bold"))
    intel_value_label.grid(row=8, column=2, padx=30, pady=5,columnspan=2)
    intel_inc_up_btn = customtkinter.CTkButton(master=creator, text = '+',command=lambda:incrementStatsUp(intel_value_label,attribute_points), font=('papyrus',18,'bold'),width=10)
    intel_inc_up_btn.grid(row=8,column=2,padx=1,sticky=E,columnspan=2)
    # intel_inc_down_btn = customtkinter.CTkButton(master=creator, text = '-',command=lambda:decrementStatsDown(intel_value_label,attribute_points), font=('papyrus',18,'bold'),width=10)
    # intel_inc_down_btn.grid(row=8,column=2,padx=1,sticky=E,columnspan=2)

    stat_const_label = customtkinter.CTkLabel(master=creator, text="Constitution:", font=("papyrus", 18, "bold"))
    stat_const_label.grid(row=10, column=1, padx=30, pady=5)
    const_value_label = customtkinter.CTkLabel(master=creator, text="0",font=('papyrus',18,'bold'))
    const_value_label.grid(row=10, column=2, padx=30, pady=5,columnspan=2)
    const_inc_up_btn = customtkinter.CTkButton(master=creator, text = '+',command=lambda:incrementStatsUp(const_value_label,attribute_points), font=('papyrus',18,'bold'),width=10)
    const_inc_up_btn.grid(row=10,column=2,padx=1,sticky=E,columnspan=2)
    # const_inc_down_btn = customtkinter.CTkButton(master=creator, text = '-',command=lambda:decrementStatsDown(const_value_label,attribute_points), font=('papyrus',18,'bold'),width=10)
    # const_inc_down_btn.grid(row=10,column=2,padx=1,sticky=E,columnspan=2)

    #roll stats button that calls rollStats
    roll_stats_btn = customtkinter.CTkButton( master=creator,text="Roll Stats",font=('papyrus',18,'bold'),command=lambda: rollStats(stren_value_label, dexty_value_label, intel_value_label, const_value_label,rollStats_counter,attribute_points))
    roll_stats_btn.grid(row=12, column=2, ipadx=15, ipady=15,columnspan=2,pady=10)
    rollStats_counter_label = customtkinter.CTkLabel(master=creator,text=rollStats_counter,font=('papyrus',24,'bold'),text_color='green')
    rollStats_counter_label.grid(row=13,column=2,columnspan=2)
    rollStats_counter_description=customtkinter.CTkLabel(master=creator,text='Stat Rolls Left:',font=('papyrus',18,'bold'))
    rollStats_counter_description.grid(row=13,column=1)

    attribute_points_description=customtkinter.CTkLabel(master=creator,text='Available Points',font=('papyrus',18,'bold'))
    attribute_points_description.grid(row=6,column=5,padx=40)
    attribute_points_label = customtkinter.CTkLabel(master=creator,text=attribute_points,font=('papyrus',18,'bold'))
    attribute_points_label.grid(row=8, column=5,padx=40)

    submitCharacter_btn = customtkinter.CTkButton(master=creator,text='Create',command=lambda: submitCharacter(),font=('papyrus',22,'bold'))
    submitCharacter_btn.grid(row=14,column=2,pady=50,padx=20,ipadx=20,ipady=10,columnspan=2)

    # prevents user from creating extra attribute points with the decrement buttons before assigning any points
    # stren_inc_down_btn.configure(state=DISABLED)
    # dexty_inc_down_btn.configure(state=DISABLED)
    # # intel_inc_down_btn.configure(state=DISABLED)
    # # const_inc_down_btn.configure(state=DISABLED)
   

mainMenu_title = customtkinter.CTkLabel(master=root, text="Main Menu", font=("Papyrus", 34, "bold"))
mainMenu_title.pack()

createPlayer_btn = customtkinter.CTkButton(master=root,text="Create Character",font=("Papyrus", 12, "bold"),command=characterCreator,)
createPlayer_btn.pack(padx=30, pady=20)

play_btn = customtkinter.CTkButton(master=root, text="Play", font=("Papyrus", 12, "bold"), command=game)
play_btn.pack(padx=30, pady=20)

load_btn = customtkinter.CTkButton(master=root,text="Load Character",font=("Papyrus", 12, "bold"),command=loadCharacter,)
load_btn.pack(padx=30, pady=20)

# commit changes
conn.commit()
conn.close()

root.mainloop()
