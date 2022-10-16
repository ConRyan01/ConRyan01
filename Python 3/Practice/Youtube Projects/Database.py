from logging import PlaceHolder
from sre_parse import State
from tkinter import *
from turtle import update
from PIL import ImageTk,Image
import sqlite3

root = Tk()
root.title("Connor's Database project")
root.iconbitmap('C:/Py Images/Witcher.ico')
root.geometry('400x400')

# create a database or connect one
conn = sqlite3.connect('address_book.db')

#create cursor - a cursor fetches data between program and DB
c = conn.cursor()

#create table

# c.execute('''CREATE TABLE addresses (  #only need to execute this once 
#     first_name text,
#     last_name text,
#     address text,
#     city text,
#     state text,
#     zipcode integer)''')

#create update function
def update():
    # create a database or connect one
    conn = sqlite3.connect('address_book.db')

    #create cursor - a cursor fetches data between program and DB
    c = conn.cursor()

    record_id = delete_box.get()
    c.execute("""UPDATE addresses SET
    first_name = :first,
    last_name = :last,
    address = :address,
    city = :city,
    state = :state,
    zipcode = :zipcode

    WHERE oid = :oid""",
    {
    'first':f_name_editor.get(),
    'last':l_name_editor.get(),
    'address':address_editor.get(),
    'city':city_editor.get(),
    'state':state_editor.get(),
    'zipcode':zipcode_editor.get(),

    'oid':record_id
    })

    #commit changes
    conn.commit()

    #close connection
    conn.close()

    editor.destroy()

#create edit function to update a record
def edit():
    global editor
    editor = Tk()
    editor.title("Update a Record")
    editor.iconbitmap('C:/Py Images/Witcher.ico')
    editor.geometry('400x300')

    # create a database or connect one
    conn = sqlite3.connect('address_book.db')

    #create cursor - a cursor fetches data between program and DB
    c = conn.cursor()

    record_id = delete_box.get()
    #query the database
    c.execute("SELECT * FROM addresses WHERE oid = " + record_id)
    records = c.fetchall()
  
    print_records = ''
    for record in records:
        print_records += str(record ) + '\n'

    #create global cariables for text box names
    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor

    #create text boxes
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0,column=1, padx = 20,pady=(10,0) )
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1,column=1, padx = 20)
    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2,column=1, padx = 20)
    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3,column=1, padx = 20)
    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4,column=1, padx = 20)
    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=5,column=1, padx = 20)

    #create text box labels
    f_name_label = Label(editor, text='first name')
    f_name_label.grid(row=0,column=0,pady=(10,0))
    l_name_label = Label(editor, text='last name')
    l_name_label.grid(row=1,column=0)
    address_label = Label(editor, text='address')
    address_label.grid(row=2,column=0)
    city_label = Label(editor, text='city')
    city_label.grid(row=3,column=0)
    state_label = Label(editor, text='state')
    state_label.grid(row=4,column=0)
    zipcode_label = Label(editor, text='zipcode')
    zipcode_label.grid(row=5,column=0)

    #loop through results
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])


    #create a save button
    edit_btn = Button(editor, text = 'Save Records', command = update)
    edit_btn.grid(row = 6, column = 0, columnspan=2, pady=10, padx=10, ipadx= 135)


#create function to delete record
def delete():
    # create a database or connect one
    conn = sqlite3.connect('address_book.db')
    #create cursor - a cursor fetches data between program and DB
    c = conn.cursor()

    c.execute('DELETE from addresses WHERE oid = ' + delete_box.get())


    #commit changes
    conn.commit()

    #close connection
    conn.close()

#create submit function
def submit():
    # create a database or connect one
    conn = sqlite3.connect('address_book.db')
    #create cursor - a cursor fetches data between program and DB
    c = conn.cursor()

    #insert into table
    c.execute('INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)',
        {
            'f_name':f_name.get(),
            'l_name':l_name.get(),
            'address':address.get(),
            'city':city.get(),
            'state':state.get(),
            'zipcode':zipcode.get()
        })


    #commit changes
    conn.commit()

    #close connection
    conn.close()

    #clear the text boxes
    f_name.delete(0,END)
    l_name.delete(0,END)
    address.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    zipcode.delete(0,END)

#create query function
def query():
    # create a database or connect one
    conn = sqlite3.connect('address_book.db')

    #create cursor - a cursor fetches data between program and DB
    c = conn.cursor()

    #query the database
    c.execute("SELECT *, oid FROM addresses") #oid selects unique entries cause there may be multiple same names
    records = c.fetchall()
    #print (records)

    print_records = ''
    for record in records:
        print_records += str(record ) + '\n'

    query_label = Label(root, text = print_records)
    query_label.grid(row = 12, column=0, columnspan=2)

    #commit changes
    conn.commit()

    #close connection
    conn.close()

#create text boxes
f_name = Entry(root, width=30)
f_name.grid(row=0,column=1, padx = 20,pady=(10,0) )
l_name = Entry(root, width=30)
l_name.grid(row=1,column=1, padx = 20)
address = Entry(root, width=30)
address.grid(row=2,column=1, padx = 20)
city = Entry(root, width=30)
city.grid(row=3,column=1, padx = 20)
state = Entry(root, width=30)
state.grid(row=4,column=1, padx = 20)
zipcode = Entry(root, width=30)
zipcode.grid(row=5,column=1, padx = 20)

delete_box = Entry(root, width=30)
delete_box.grid(row=9,column=1)

#create text box labels
f_name_label = Label(root, text='first name')
f_name_label.grid(row=0,column=0,pady=(10,0))
l_name_label = Label(root, text='last name')
l_name_label.grid(row=1,column=0)
address_label = Label(root, text='address')
address_label.grid(row=2,column=0)
city_label = Label(root, text='city')
city_label.grid(row=3,column=0)
state_label = Label(root, text='state')
state_label.grid(row=4,column=0)
zipcode_label = Label(root, text='zipcode')
zipcode_label.grid(row=5,column=0)
delete_box_label = Label(root, text='Select ID')
delete_box_label.grid(row=9,column=0,pady=(0,5))

#create submit button
submit_btn = Button(root, text='Add Record to Database', command=submit)
submit_btn.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=105)

#create a query button
query_btn = Button(root, text = 'Show records', command = query)
query_btn.grid(row = 8, column = 0, columnspan=2, pady=10, padx=10, ipadx= 135)

#create a delete button
delete_btn = Button(root, text = 'Delete Record', command = delete)
delete_btn.grid(row = 10, column = 0, columnspan=2, pady=10, padx=10, ipadx= 134)

#create an update button
delete_btn = Button(root, text = 'Update Record', command = edit)
delete_btn.grid(row = 11, column = 0, columnspan=2, pady=10, padx=10, ipadx= 134)

#commit changes
conn.commit()

#close connection
conn.close()

mainloop()

