import requests
import tkinter as tk
from PIL import ImageTk,Image

report_data=[]
def get_report():
    location = input_box.get()
    url="https://api.openweathermap.org/data/2.5/weather?q={}&APPID="Your-API-Key"&units=metric".format(location)
    try:
        response= requests.get(url)
        status= response.status_code
        if status == 200:
            data=response.json()
            description= data["weather"][0]["description"]
            main=data["main"]
            temperature = main["temp"]
            feels_like =  main["feels_like"]
            humidity = main["humidity"]
            wind_speed = data["wind"]["speed"]
            country = data["sys"]["country"]
            
            clear()
            title= tk.Label(root,text=f"\nWEATHER REPORT FOR: {location.title()},{country}",bg="black",font=("verdana",14),fg="white")
            title.pack()
            report_data.append(title)
            description=tk.Label(root, text=f"Condition: {description.title()}",bg="black",font=("verdana",14),fg="white")
            description.pack()
            report_data.append(description)
            temp=tk.Label(root, text=f"Temperature: {temperature}°C feels like {feels_like}°C",bg="black",font=("verdana",14),fg="white")
            temp.pack()
            report_data.append(temp)
            humidity=tk.Label(root, text=f"Humidity: {humidity}",bg="black",font=("verdana",14),fg="white")
            humidity.pack()
            report_data.append(humidity)
            speed=tk.Label(root, text=f"Wind Speed: {wind_speed}",bg="black",font=("verdana",14),fg="white")
            speed.pack()
            report_data.append(speed)
        


        elif status == 404:
            tk.Label(root, text="Invalid City Name! Please Enter a Valid City Name",bg="black",font=("verdana",14),fg="white").pack()

        elif status == 401:
            tk.Label(root, text="API Error!",bg="black",font=("verdana",14),fg="white").pack()

        else:
            tk.Label(root, text="Something Went Wrong.",bg="black",font=("verdana",14),fg="white").pack()

    except requests.exceptions.ConnectionError:
        tk.Label(root, text="Sorry! Connection Error!",bg="black",font=("verdana",14),fg="white").pack()
    except requests.exceptions.RequestException:
        tk.Label(root, text="Something went wrong with the network request.",bg="black",font=("verdana",14),fg="white").pack()
    except Exception:
        tk.Label(root, text="Something went wrong.",bg="black",font=("verdana",14),fg="white").pack()

def clear():
    for label in report_data:
        label.destroy()

    report_data.clear()


root= tk.Tk()
root.title("My Weather APP")
root.configure(background="black")

root.geometry("300x400")
root.maxsize(500,600)
root.minsize(500,600)
text_label= tk.Label(root, text="MY WEATHER APP",fg="white",font="verdana",justify="center", pady=20,bg="black")
text_label.pack()
img = Image.open("logo.png")
img = img.resize((150,150))
img = ImageTk.PhotoImage(img)
img_label= tk.Label(root,image=img,bg="black")
img_label.pack(pady=10)
input_box = tk.Entry(root, width=30)
input_box.pack(pady=10)
check_weather = tk.Button(bg="Orange",fg="white",font=("verdana",16),text="Get Report", justify="center",height=1,command=get_report)
check_weather.pack(pady=15)
root.mainloop()
