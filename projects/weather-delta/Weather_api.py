import requests
import time
from datetime import datetime

API_KEY = ""
LAT = "26.199416"
LON = "50.183513"
#exclude = "minutely,hourly,daily,alerts"
#PART = exclude
main_url = f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={API_KEY}&units=metric"

def get_response():
    try:
        response = requests.get(main_url)
        if response.status_code == 200:
            data = response.json()
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            time_str = datetime.fromtimestamp(data["dt"]).strftime("%Y-%m-%d %H:%M:%S")
            print(f"Temp: {temp}°C")
            print(f"Humidity: {humidity}%")
            print(f"Time: {time_str}")
            with open("record.txt", "a") as f:
                f.write(f"Time: {time_str}\n")
                f.write(f"Temp: {temp}°C\n")
                f.write(f"Humidity: {humidity}%\n")
                f.write("########################################\n")
        else:
            print(f"Failed: {response.status_code}")
    except requests.exceptions.ConnectionError:
        print("No internet connection, retrying...")
        

while True:
    get_response()
    time.sleep(600)
