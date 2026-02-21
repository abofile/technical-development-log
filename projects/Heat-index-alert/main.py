import dht
from machine import I2C, Pin
import time
from lcd_i2c import LCD
# Heat Index Lookup Table
# Structure: HEAT_INDEX_TABLE[air_temp_c][relative_humidity_%] = heat_index
# None = off-chart (automatically Extreme Danger IV, treat as 52+)

HEAT_INDEX_TABLE = {
    51: {10:None,20: None, 30: None, 40: None, 50: None, 60: None, 70: None, 80: None, 90: None},
    50: {10: 48, 20: None, 30: None, 40: None, 50: None, 60: None, 70: None, 80: None, 90: None},
    49: {10: 47, 20: None, 30: None, 40: None, 50: None, 60: None, 70: None, 80: None, 90: None},
    48: {10: 45, 20: 53,   30: None, 40: None, 50: None, 60: None, 70: None, 80: None, 90: None},
    47: {10: 44, 20: 51,   30: None, 40: None, 50: None, 60: None, 70: None, 80: None, 90: None},
    46: {10: 43, 20: 49,   30: None, 40: None, 50: None, 60: None, 70: None, 80: None, 90: None},
    45: {10: 42, 20: 47,   30: None, 40: None, 50: None, 60: None, 70: None, 80: None, 90: None},
    44: {10: 41, 20: 46,   30: 52,   40: None, 50: None, 60: None, 70: None, 80: None, 90: None},
    43: {10: 40, 20: 44,   30: 49,   40: None, 50: None, 60: None, 70: None, 80: None, 90: None},
    42: {10: 39, 20: 42,   30: 47,   40: 54,   50: None, 60: None, 70: None, 80: None, 90: None},
    41: {10: 38, 20: 41,   30: 45,   40: 51,   50: None, 60: None, 70: None, 80: None, 90: None},
    40: {10: 37, 20: 39,   30: 43,   40: 48,   50: None, 60: None, 70: None, 80: None, 90: None},
    39: {10: 36, 20: 38,   30: 41,   40: 46,   50: 52,   60: None, 70: None, 80: None, 90: None},
    38: {10: 35, 20: 37,   30: 39,   40: 43,   50: 49,   60: 55,   70: None, 80: None, 90: None},
    37: {10: 34, 20: 35,   30: 38,   40: 41,   50: 46,   60: 51,   70: None, 80: None, 90: None},
    36: {10: 33, 20: 34,   30: 36,   40: 39,   50: 43,   60: 48,   70: 54,   80: None, 90: None},
    35: {10: 32, 20: 33,   30: 35,   40: 37,   50: 41,   60: 45,   70: 50,   80: None, 90: None},
    34: {10: 31, 20: 32,   30: 33,   40: 35,   50: 38,   60: 42,   70: 47,   80: 52,   90: None},
    33: {10: 31, 20: 31,   30: 32,   40: 34,   50: 36,   60: 40,   70: 44,   80: 48,   90: 54  },
    32: {10: 30, 20: 30,   30: 31,   40: 32,   50: 34,   60: 37,   70: 40,   80: 44,   90: 49  },
    31: {10: 29, 20: 29,   30: 30,   40: 31,   50: 33,   60: 35,   70: 38,   80: 41,   90: 45  },
    30: {10: 28, 20: 28,   30: 29,   40: 30,   50: 31,   60: 33,   70: 35,   80: 38,   90: 41  },
    29: {10: 27, 20: 27,   30: 28,   40: 29,   50: 30,   60: 31,   70: 33,   80: 35,   90: 37  },
    28: {10: 27, 20: 27,   30: 27,   40: 28,   50: 28,   60: 29,   70: 31,   80: 32,   90: 34  },
    27: {10: 26, 20: 26,   30: 26,   40: 27,   50: 27,   60: 28,   70: 29,   80: 30,   90: 31  },
    26: {10: 25, 20: 25,   30: 26,   40: 26,   50: 27,   60: 27,   70: 27,   80: 28,   90: 28  },
    25: {10: 25, 20: 25,   30: 25,   40: 25,   50: 25,   60: 25,   70: 25,   80: 25,   90: 25  },
}


# To Check If LCD Is begin detected
#i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=800000)
#print(i2c.scan()) 
# init the lcd
I2C_ADDR = 0x27
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=800000)
lcd = LCD(addr=I2C_ADDR, cols=16, rows=2, i2c=i2c)
lcd.begin()



while True:
    time.sleep(2)
    

    #sensor setup
    d = dht.DHT22(Pin(4))
    d.measure()
    temp_input = d.temperature()
    humid_input = d.humidity()

    #print(f"actual temp: {round(temp_input,1)}  actual humid: {round(humid_input,1)}")

    # to switch the sensor input to int for compatability with HEAT_INDEX_TABLE
    air_temp_c = int(temp_input)
    relative_humidity = int(humid_input)

    temp = 0
    humid = 0

    def out_of_range_round(tempc,air_moisture):
        global temp
        global humid
        temp = tempc
        humid = air_moisture

        if temp not in range(26,51):
            if temp < 26:
                temp = 25
            else:
                temp = 51

        if humid not in range(10,91):
            if humid < 10:
                humid = 10
            else:
                humid = 90
        else:
            pass

    out_of_range_round(air_temp_c,relative_humidity)
    #print(f"conv temp: {round(temp,1)}  conv humid: {round(humid, -1)}")
    HEAT_INDEX = HEAT_INDEX_TABLE[temp][round(humid,-1)]

    
    lcd.clear()
    if HEAT_INDEX is None or HEAT_INDEX >= 52:
        lcd.set_cursor(0, 0)
        lcd.print(f"Temp:{temp_input}Humi:{humid_input}")
        lcd.set_cursor(0, 1)
        lcd.print("Extreme Danger IV")
    if HEAT_INDEX <= 25:
        lcd.set_cursor(0, 0)
        lcd.print(f"Temp:{temp_input} humi:{humid_input}")
        lcd.set_cursor(0, 1)
        lcd.print("Normal Condition")

    elif HEAT_INDEX <= 29:
        lcd.set_cursor(0, 0)
        lcd.print(f"Temp:{round(temp_input,1)}Humi:{round(humid_input,1)}")
        lcd.set_cursor(0, 1)
        lcd.print("Caution I")

    elif 30 <= HEAT_INDEX <= 38:
        lcd.set_cursor(0, 0)
        lcd.print(f"Temp:{temp_input}Humi:{humid_input}")
        lcd.set_cursor(0, 1)
        lcd.print("Extreme Caution II")
    elif 39 <= HEAT_INDEX <= 51:
        lcd.set_cursor(0, 0)
        lcd.print(f"Temp:{temp_input}Humi:{humid_input}")
        lcd.set_cursor(0, 1)
        lcd.print("Danger III")
   
