import sqlite3
import requests
import time
from datetime import datetime

API_KEY = ""
LAT = ""
LON = ""

main_url = f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={API_KEY}&units=metric"

def get_response():
    try:
        response = requests.get(main_url)
        data = response.json()
        if response.status_code == 200:
            with sqlite3.connect("weather_log.db") as conn:
                conn.execute("""
                    CREATE TABLE IF NOT EXISTS weather_log (
                        id          INTEGER PRIMARY KEY AUTOINCREMENT,
                        temp        REAL,
                        humidity    INTEGER,
                        recorded_at TEXT
                    )
                """)
                conn.execute(
                    "INSERT INTO weather_log (temp, humidity, recorded_at) VALUES (?, ?, ?)",
                    (data["main"]["temp"], data["main"]["humidity"], datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                )
        else:
            print(f"Failed: {response.status_code}")
    except requests.exceptions.ConnectionError:
        print("No internet connection, retrying...")      

while True:
    get_response()
    time.sleep(1)
