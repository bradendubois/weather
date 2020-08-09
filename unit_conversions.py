from json import load

MARGIN = 22.5

with open("config.json") as f:
    temperature_unit = load(f)["temperature_unit"].lower()

assert temperature_unit in ["kelvin", "celsius", "fahrenheit"]

def kelvin_to_kelvin(temperature: float):
    return temperature

def kelvin_to_celsius(temperature: float):
    return temperature - 273.15

def kelvin_to_fahrenheit(temperature: float):
    return temperature * 9 / 5 - 459.67

if temperature_unit == "kelvin":
    temperature_conversion = kelvin_to_kelvin
elif temperature_unit == "celsius":
    temperature_conversion = kelvin_to_celsius
else:
    temperature_conversion = kelvin_to_fahrenheit

def wind_speed_conversion(speed: float):
    # TODO - What units does the API provide it in?
    return speed

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
