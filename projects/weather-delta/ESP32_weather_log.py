import bme280_float as bme280
from machine import I2C, Pin
import time
from umqtt.robust import MQTTClient


i2c = I2C(0, sda=Pin(21), scl=Pin(22))
bme = bme280.BME280(i2c=i2c)


def read_log_data(server="Broker local host"):
    temp, pressure, humidity = bme.values
    c = MQTTClient("ESP-32", server)
    
    c.connect()
    c.publish(b"sensors/temp", str(temp).encode())
    c.publish(b"sensors/humidity", str(humidity).encode())
    c.publish(b"sensors/pressure", str(pressure).encode())
    c.disconnect()


def do_connect():
    import machine, network
    wlan = network.WLAN()
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('ssid', 'pass')
        while not wlan.isconnected():
            machine.idle()
    print('network config:', wlan.ipconfig('addr4'))


while True:
    do_connect()
    read_log_data(server="")
    time.sleep(5)


    
