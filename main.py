from tkinter import*
import tkinter as tk
from tkinter import messagebox
import requests
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import pytz
import pyttsx3
global bgc 
bgc = "#f4c2c2"
#tkinter setup
root = Tk()
root.title("weather app")
root.geometry("1000x600+300+150")
root.resizable(False,False)
engine = pyttsx3.init() #text to speech
#functions for configuring theme
def blueTheme():
    root.config(bg = "#89CFF0")
    myLabel.config(bg = "#89CFF0")
    myLabel11.config(bg = "#89CFF0")
    myLabel33.config(bg = "#89CFF0")
    myLabel44.config(bg = "#89CFF0")
    myimage.config(bg = "#89CFF0")
    myimage_icon.config(bg = "#89CFF0")
    frame_myimage.config(bg = "#89CFF0")
    clock.config(bg = "#89CFF0")
    t.config(bg = "#89CFF0")
    c.config(bg = "#89CFF0")
    myLabelic.config(bg = "#89CFF0")
    myLabelic1.config(bg = "#89CFF0")
    myLabelic2.config(bg = "#89CFF0")
    myLabelic3.config(bg = "#89CFF0")
    myLabelic4.config(bg = "#89CFF0")
    myLabelic5.config(bg = "#89CFF0")
def defaultTheme():
    root.config(bg = "#f4c2c2")
    myLabel.config(bg = "#f4c2c2")
    myLabel11.config(bg = "#f4c2c2")
    myLabel33.config(bg = "#f4c2c2")
    myLabel44.config(bg = "#f4c2c2")
    myimage.config(bg = "#f4c2c2")
    myimage_icon.config(bg = "#f4c2c2")
    frame_myimage.config(bg = "#f4c2c2")
    clock.config(bg = "#f4c2c2")
    t.config(bg = "#f4c2c2")
    c.config(bg = "#f4c2c2")
    myLabelic.config(bg = "#f4c2c2")
    myLabelic1.config(bg = "#f4c2c2")
    myLabelic2.config(bg = "#f4c2c2")
    myLabelic3.config(bg = "#f4c2c2")
    myLabelic4.config(bg = "#f4c2c2")
    myLabelic5.config(bg = "#f4c2c2")
def greenTheme():
    root.config(bg = "#d9f4ed")
    myLabel.config(bg = "#d9f4ed")
    myLabel11.config(bg = "#d9f4ed")
    myLabel33.config(bg = "#d9f4ed")
    myLabel44.config(bg = "#d9f4ed")
    myimage.config(bg = "#d9f4ed")
    myimage_icon.config(bg = "#d9f4ed")
    frame_myimage.config(bg = "#d9f4ed")
    clock.config(bg = "#d9f4ed")
    t.config(bg = "#d9f4ed")
    c.config(bg = "#d9f4ed")
    myLabelic.config(bg = "#d9f4ed")
    myLabelic1.config(bg = "#d9f4ed")
    myLabelic2.config(bg = "#d9f4ed")
    myLabelic3.config(bg = "#d9f4ed")
    myLabelic4.config(bg = "#d9f4ed")
    myLabelic5.config(bg = "#d9f4ed")
def greyTheme():
    root.config(bg = "#d3d3d3")
    myLabel.config(bg = "#d3d3d3")
    myLabel11.config(bg = "#d3d3d3")
    myLabel33.config(bg = "#d3d3d3")
    myLabel44.config(bg = "#d3d3d3")
    myimage.config(bg = "#d3d3d3")
    myimage_icon.config(bg = "#d3d3d3")
    frame_myimage.config(bg = "#d3d3d3")
    clock.config(bg = "#d3d3d3")
    t.config(bg = "#d3d3d3")
    c.config(bg = "#d3d3d3")
    myLabelic.config(bg = "#d3d3d3")
    myLabelic1.config(bg = "#d3d3d3")
    myLabelic2.config(bg = "#d3d3d3")
    myLabelic3.config(bg = "#d3d3d3")
    myLabelic4.config(bg = "#d3d3d3")
    myLabelic5.config(bg = "#d3d3d3")
def darkTheme():
    root.config(bg = "black")
    myLabel.config(bg = "black")
    myLabel11.config(bg = "black")
    myLabel33.config(bg = "black")
    myLabel44.config(bg = "black")
    myimage.config(bg = "black")
    myimage_icon.config(bg = "black")
    frame_myimage.config(bg = "black")
    clock.config(bg = "black")
    t.config(bg = "black")
    c.config(bg = "black")
    myLabelic.config(bg = "black")
    myLabelic1.config(bg = "black")
    myLabelic2.config(bg = "black")
    myLabelic3.config(bg = "black")
    myLabelic4.config(bg = "black")
    myLabelic5.config(bg = "black")
def lightTheme():
    root.config(bg = "white")
    myLabel.config(bg = "white")
    myLabel11.config(bg = "white")
    myLabel33.config(bg = "white")
    myLabel44.config(bg = "white")
    myimage.config(bg = "white")
    myimage_icon.config(bg = "white")
    frame_myimage.config(bg = "white")
    clock.config(bg = "white")
    t.config(bg = "white")
    c.config(bg = "white")
    myLabelic.config(bg = "white")
    myLabelic1.config(bg = "white")
    myLabelic2.config(bg = "white")
    myLabelic3.config(bg = "white")
    myLabelic4.config(bg = "white")
    myLabelic5.config(bg = "white")
root.configure(bg =bgc)
root.iconbitmap('icon.ico')
#some images
bg = PhotoImage(file="svg.png")
myLabel = Label(root, image = bg, bg=bgc)
myLabel.place(x=0,y= 0)

bg11 = PhotoImage(file="svg.png")
myLabel11 = Label(root, image = bg11, bg=bgc)
myLabel11.place(x=930,y= 350)


bg33 = PhotoImage(file="sun.png")
myLabel33 = Label(root, image = bg33, bg=bgc)
myLabel33.place(x=0,y= 300)

bg44 = PhotoImage(file="moon.png")
myLabel44 = Label(root, image = bg44, bg=bgc)
myLabel44.place(x=850,y= 40)

#function to retrieve weather info
def getWeather():
    try:
        city=textfield.get()
        #date time
        geolocator= Nominatim(user_agent="geoapiExercises")
        location= geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude,lat=location.latitude) #timezone format of city
        
        home=pytz.timezone(result)#timezone
        local_time=datetime.now(home)
        current_time=local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        

        #weather
        #condition, description, temp, pressure, humidity, wind, icon
        api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=06c921750b9a82d8f5d1294e1586276f"

        json_data = requests.get(api).json()
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp']-273.15)
        icon = json_data['weather'][0]['icon']

        ic.config(file = f"weather_icons/{icon}.png")
        ic1.config(file = f"weather_icons/{icon}.png")
        ic2.config(file = f"weather_icons/{icon}.png")
        ic3.config(file = f"weather_icons/{icon}.png")
        ic4.config(file = f"weather_icons/{icon}.png")
        ic5.config(file = f"weather_icons/{icon}.png")       
        t.config(text=(temp,"°"))
        c.config(text=(description))
        p.config(text="\0")
        h.config(text="\0")
        engine.say(f"Weather feels like {temp} °")
        engine.runAndWait()
        
    except Exception as e:
        messagebox.showerror("Weather App", "enter correct city name")  

#Functions for features
def getHumidity():
    try:
        city=textfield.get()
        api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=06c921750b9a82d8f5d1294e1586276f"

        json_data = requests.get(api).json()
        humidity = json_data['main']['humidity']
        p.config(text="\0")
        h.config(text=f"{humidity} % humid")

    except Exception as e:
        messagebox.showerror("enter city name")

def getPressure():
    try:
        city=textfield.get()
        api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=06c921750b9a82d8f5d1294e1586276f"

        json_data = requests.get(api).json()
        pressure = json_data['main']['pressure']
        h.config(text="\0")
        p.config(text=f"{pressure} mb")

    except Exception as e:
        messagebox.showerror("enter city name")

def getHelp():
    messagebox.showinfo("Usage", "Enter city name & find weather info")


#search field
Search_image = PhotoImage(file="src2.png")
myimage = Label(image=Search_image, bg =bgc)
myimage.place(x=55, y=-301)

textfield = tk.Entry(root,justify="center",width=17,font=("Comic Sans MS",35,"bold"),bg="#fff",border=0,fg="#528aff")
textfield.place(x=200,y=20)
textfield.focus()

Search_icon = PhotoImage(file="srchnew.png")
myimage_icon=Button(image=Search_icon,borderwidth=0,cursor="hand2",bg=bgc,command=getWeather)
myimage_icon.place(x=750,y=0)


#Bottom field
Frame_image=PhotoImage(file="realbox.png")
frame_myimage=Label(image=Frame_image, bg=bgc)
frame_myimage.place(x=180,y=420)

#time
clock=Label(root,font=("Helvetica",20),fg = "#00aeef", bg=bgc)
clock.place(x=30,y=230)

#temperature & description
t=Label(text="",font=("Comic Sans MS",50,"bold"),fg="#DE3163", bg=bgc)
t.place(x=400,y=230)
c=Label(font=("Comic Sans MS",15,'bold'), bg=bgc )
c.place(x=500,y=280)

#h/p
h=Label(text="\0",font=("ArcadeClassic",50,"bold"),fg="#93C572",bg='white')
h.place(x=400,y=490)
p=Label(text="\0",font=("ArcadeClassic",50,"bold"),fg="#89CFF0",bg='white')
p.place(x=270,y=490)


#icons
#bottom3
ic = PhotoImage(file="")
myLabelic = Label(root, image = ic,bg=bgc)
myLabelic.place(x=590,y= 360)

ic1 = PhotoImage(file="")
myLabelic1 = Label(root, image = ic1,bg=bgc)
myLabelic1.place(x=450,y= 360)

ic2 = PhotoImage(file="")
myLabelic2 = Label(root, image = ic2,bg=bgc)
myLabelic2.place(x=310,y= 360)

#upper3
ic3 = PhotoImage(file="")
myLabelic3 = Label(root, image = ic3,bg=bgc)
myLabelic3.place(x=590,y= 110)

ic4 = PhotoImage(file="")
myLabelic4 = Label(root, image = ic4,bg=bgc)
myLabelic4.place(x=450,y= 110)

ic5 = PhotoImage(file="")
myLabelic5 = Label(root, image = ic5,bg=bgc)
myLabelic5.place(x=310,y= 110)

#dropdown menu
mainmenu = Menu(root)
m1 = Menu(mainmenu, tearoff=0)
m1.add_command(label="Humidity", command=getHumidity)
m1.add_command(label="Pressure", command=getPressure)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="H/P", menu=m1)
m2 = Menu(mainmenu, tearoff=0)
m2.add_command(label="Default", command=defaultTheme)
m2.add_command(label="Dark", command=darkTheme)
m2.add_command(label="Light", command=lightTheme)
m2.add_command(label="Blue", command=blueTheme)
m2.add_command(label="Green", command=greenTheme)
m2.add_command(label="Grey", command=greyTheme)
mainmenu.add_cascade(label="Theme", menu=m2)
m3 = Menu(mainmenu, tearoff=0)
m3.add_command(label="Usage",command=getHelp)
mainmenu.add_cascade(label="Help", menu=m3)

root.mainloop()