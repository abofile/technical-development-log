# weather-delta

A Python tool that compares averaged local sensor readings from an ESP32 against public weather API data for the same area, and logs both to a SQLite database for delta tracking over time.

## How It Works

- The ESP32 reads temperature, humidity, and pressure from a BME280 sensor every minute for 10 minutes
- The 10 readings are averaged to reduce noise and improve accuracy
- The OpenWeatherMap API is called once at the end of the 10-minute window
- Both the averaged sensor data and the API data are logged to a SQLite database with a timestamp
- The delta between the two sources is calculated and stored for all three readings

## Planned Stack

| Part | Tool |
|---|---|
| Language | Python 3 |
| Microcontroller | ESP32 |
| Sensor | BME280 |
| Weather data | OpenWeatherMap API (free tier) |
| Data format | JSON |
| Logging | SQLite |

## Project Goals

This project is primarily a learning exercise targeting:

- Working with public REST APIs
- Parsing and handling JSON responses
- WiFi communication via ESP32
- SQLite database logging from both API and hardware sources
- Averaging sensor data for accuracy
- Basic data comparison and delta calculation

