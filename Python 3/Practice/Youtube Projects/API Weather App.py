from tkinter import *
from turtle import back
from webbrowser import get
from PIL import ImageTk,Image
import requests
import json

#main purpose of this is to learn how to connecto to API
root = Tk()
root.title("Connor's Weather App")
root.iconbitmap('C:/Py Images/Witcher.ico')
root.geometry('600x100')

#create zipcode lookup function
def zipLookup():
    #zip.get()
    #zipLabel = Label(root, text = zip.get())
    #zipLabel.grid(row=1,column=0,columnspan=2)

    #https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=19805&distance=25&API_KEY=3775884B-6926-49E1-81ED-0840409D51C5

    try:
        
        api_request= requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip.get() + "&distance=25&API_KEY=3775884B-6926-49E1-81ED-0840409D51C5")
        api = json.loads(api_request.content)
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']

        if category == 'Good':
            weather_color = '#00e400'
        elif category == 'Moderate':
            weather_color = '#ffff00'
        elif category == 'Unhealthy for Sensitive Groups':
            weather_color = '#ff7e00'
        elif category == 'Unhealthy':
            weather_color = '#ff0000'
        elif category == 'Very Unhealthy':
            weather_color = '#8f3f97'
        elif category == 'Hazardous':
            weather_color = '#7e0023'

        root.configure(background=weather_color)

        myLabel = Label(root, text=city + ' Air Quality ' + str(quality) + ' ' + category, font=('Helvetica',20), background=weather_color)
        myLabel.grid(row=1,column=0,columnspan=2)

    except Exception as e:
        api = 'Error...'

zip = Entry(root)
zip.grid(row = 0, column = 0, sticky=W+E+S+N)

zipButton = Button (root, text = 'Lookup Zipcode', command = zipLookup)
zipButton.grid(row = 0, column= 1, sticky=W+N+S+E)

root.mainloop()

