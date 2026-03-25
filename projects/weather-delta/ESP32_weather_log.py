import bme280_float as bme280
from machine import I2C, Pin
import time


i2c = I2C(0, sda=Pin(21), scl=Pin(22))
bme = bme280.BME280(i2c=i2c)
temp, pressure, humidity = bme.values


def read_log_data(temp, pressure, humidity):
    pass


def do_connect():
    import machine, network
    wlan = network.WLAN()
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('ssid', 'key')
        while not wlan.isconnected():
            machine.idle()
    print('network config:', wlan.ipconfig('addr4'))


while True:
    #do_connect()
    #read_log_data()
    pass
