#import dht 

# Heat Index Lookup Table
# Structure: HEAT_INDEX_TABLE[air_temp_c][relative_humidity_%] = heat_index
# None = off-chart (automatically Extreme Danger IV, treat as 52+)

HEAT_INDEX_TABLE = {
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
}

air_temp_c = int(input("temp"))
relative_humidity = int(input("humid"))
temp = 0
humid = 0

def out_of_range_round(tempc,air_moisture):
    global temp
    global humid
    temp = tempc
    humid = air_moisture

    if temp not in range(26,51):
        if temp < 26:
            temp = 26
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
print(f"{temp}  {humid}")
HEAT_INDEX = HEAT_INDEX_TABLE[temp][humid]



if HEAT_INDEX <= 29:
    print("Caution")
elif 30 <= HEAT_INDEX <= 38:
    print("Extreme Caution")
elif 39 <= HEAT_INDEX <= 51:
    print("Danger")
elif HEAT_INDEX >= 52:
    print("Extreme Danger")
else:
    print("Normal Condition")




