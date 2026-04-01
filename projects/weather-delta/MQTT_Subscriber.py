import sqlite3
import paho.mqtt.subscribe as subscribe
from datetime import datetime

with sqlite3.connect("weather_log.db") as conn:
    conn.execute("""
        CREATE TABLE IF NOT EXISTS weather_log_ESP (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            temp        REAL,
            humidity    REAL,
            pressure    REAL,
            recorded_at TEXT
        )
    """)

data = {}

def on_message(client, _, message):
    topic = message.topic
    value = float(message.payload.decode().replace("C", "").replace("%", "").replace("hPa", ""))
    
    if topic == "sensors/temp":
        data["temp"] = value
    elif topic == "sensors/humidity":
        data["humidity"] = value
    elif topic == "sensors/pressure":
        data["pressure"] = value
    
    if all(k in data for k in ["temp", "humidity", "pressure"]):
        with sqlite3.connect("weather_log.db") as conn:
            conn.execute(
                "INSERT INTO weather_log_ESP (temp, humidity, pressure, recorded_at) VALUES (?, ?, ?, ?)",
                (data["temp"], data["humidity"], data["pressure"], datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            )
        print(data)
        data.clear()

subscribe.callback(on_message, "sensors/#", hostname="local host")
