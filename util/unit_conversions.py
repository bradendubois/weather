from json import load

MARGIN = 22.5

def kelvin_to_kelvin(temperature: float):
    return temperature

def kelvin_to_celsius(temperature: float):
    return temperature - 273.15

def kelvin_to_fahrenheit(temperature: float):
    return temperature * 9 / 5 - 459.67

def wind_direction_conversion(degrees: int):

    msg = ""

    if 315 - MARGIN <= degrees or degrees <= 45 + MARGIN:
        msg += "N"
    elif 135 - MARGIN <= degrees <= 225 + MARGIN:
        msg += "S"
    
    if 45 - MARGIN <= degrees <= 135 + MARGIN:
        msg += "E"
    elif 225 - MARGIN <= degrees <= 315 + MARGIN:
        msg += "W"
    
    return msg

def wind_speed_conversion(speed: float, time, unit):

    if time == "second":
        time_conversion = 1
    elif time == "minute":
        time_conversion = 60
    elif time == "h":
        time_conversion = 3600

    if unit == "m":
        distance_conversion = 1
    elif unit == "f":
        distance_conversion = 3.281
    elif unit == "miles":
        distance_conversion = 1 / 1609
    elif unit == "km":
        distance_conversion = 1 / 1000
    
    return speed * time_conversion * distance_conversion
