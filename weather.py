from tkinter import *
import requests
from tkinter import ttk
root=Tk()
root.geometry("650x450")

f1=Frame(root,height=350,width=550,bg="lightblue")
f1.pack()
Label(f1,text="Enter your City ",fg="black",bg=f1["bg"],font=("Arial 15")).grid(row=0,column=0,padx=10)

def weatherAPI(city,weather,temperature,huminity,wind_speed):
    
    API_KEY = "Your_API_KEY"  # Replace with your actual API key
    
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        weather_data = data["weather"][0]["description"]
        temp_data = data["main"]["temp"]
        humidity_data = data["main"]["humidity"]
        wind_speed_data = data["wind"]["speed"]

        weather.delete(0,END)
        weather.insert(0,weather_data)

        temperature.delete(0,END)
        temperature.insert(0,f"{temp_data}")

        huminity.delete(0,END)
        huminity.insert(0,f"{humidity_data}%")

        
        wind_speed.delete(0,END)
        wind_speed.insert(0,f"{wind_speed_data}km/h")

        
        
        
    else:
        print("Error fetching weather data.")

gujarat_cities = [
    'Ahmedabad',
    'Surat',
    'Vadodara',
    'Rajkot',
    'Bhavnagar',
    'Jamnagar',
    'Gandhinagar',
    'Junagadh',
    'Anand',
    'Nadiad',
    'Morbi',
    'Mehsana',
    'Bharuch',
    'Vapi',
    'Porbandar'
]

city = ttk.Combobox(f1, values=gujarat_cities, state="readonly")
city.grid(row=0,column=1,pady=15,ipady=5,padx=15)

Label(f1,text="weather",bg=f1["bg"],font=("Arial 15")).grid(row=1,column=0,padx=10)

weather=Entry(f1,width=25,font=("Arial 15"))
weather.grid(row=1,column=1,ipady=5,pady=15,padx=15)

Label(f1,text="Temperature",bg=f1["bg"],font=("Arial 15")).grid(row=2,column=0,padx=10)

temperature=Entry(f1,width=25,font=("Arial 15"))
temperature.grid(row=2,column=1,ipady=5,pady=15,padx=15)

Label(f1,text="huminity",bg=f1["bg"],font=("Arial 15")).grid(row=3,column=0,padx=10)

root.configure(bg="lightblue")

huminity=Entry(f1,width=25,font=("Arial 15"))
huminity.grid(row=3,column=1,ipady=5,pady=15,padx=15)

Label(f1,text="windspeed",bg=f1["bg"],font=("Arial 15")).grid(row=4,column=0,padx=10)

wind_speed=Entry(f1,width=25,font=("Arial 15"))
wind_speed.grid(row=4,column=1,pady=15,ipady=5,padx=15)

submit=Button(f1,height=1,width=20,text="submit",font=("Arial 15"),command=lambda:weatherAPI(city.get(),weather,temperature,huminity,wind_speed))
submit.grid(row=5,column=1)


root.mainloop()
