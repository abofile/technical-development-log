# weather-delta

A Python tool that compares local sensor readings from a Raspberry Pi Pico against public weather API data for the same area, and logs the difference over time.

## Planned Features

- Pull current weather data from a public API (OpenWeatherMap) by coordinates
- Read temperature and humidity from a DHT22 sensor on the Raspberry Pi Pico
- Compare local sensor readings against the API data
- Log the delta between the two sources with a timestamp
- Track patterns over time — does the local area consistently read hotter or more humid than the official station?

## Planned Stack

| Part | Tool |
|---|---|
| Language | Python 3 |
| Sensor | DHT22 via Raspberry Pi Pico |
| Weather data | OpenWeatherMap API (free tier) |
| Data format | JSON |
| Logging | CSV or plain text file |

## Project Goals

This project is primarily a learning exercise targeting:

- Working with public REST APIs
- Parsing and handling JSON responses
- Serial or network communication with the Pico
- File I/O for structured logging
- Basic data comparison logic

## Status

> 🔧 In planning — not yet started
