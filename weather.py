#!/usr/bin/env python

import requests
from os import path
from json import load

from util.parse_response import *
from util.print_response import print_response

root = path.dirname(path.abspath(__file__))

# Load the config file
with open(root + "/configuration.json") as f:
    data = load(f)

# API Key / City for query
api_key = data["api_key"]
city = data["city"]

# Conversion / unit data
temperature_unit = data["temperature_unit"].lower().strip()
wind_unit = data["wind_unit"].lower().strip()
wind_symbol = wind_unit

if temperature_unit == "kelvin":
    temperature_conversion = kelvin_to_kelvin
elif temperature_unit == "celsius":
    temperature_conversion = kelvin_to_celsius
else:
    temperature_conversion = kelvin_to_fahrenheit
temperature_symbol = temperature_unit[0].upper()

unit, time = [i.lower().strip() for i in wind_unit.split("/")]

# Need API key / City
if api_key == "API_KEY_HERE" or city == "CITY_HERE":
    print("Config file not fully set up.")
    exit(-1)

# Ensure temperature unit is specified
if temperature_unit not in ["kelvin", "celsius", "fahrenheit"]:
    print("Temperature units not configured.")
    exit(-1)

# Ensure valid distance to present wind in 
if unit not in ["m", "f", "miles", "km"]:
    print("Distance units not configured correctly.")
    exit(-1)
    
# Ensure valid time units to present wind speed in
if time not in ["second", "minute", "h"]:
    print("Time units not configured correctly.")
    exit(-1)
    
# URL to query the openweathermap API
url = "http://api.openweathermap.org/data/2.5/weather?appid={}&q={}".format(api_key, city)

# Make request, parse result
response = requests.get(url).json()

# 404 === location not found
if response["cod"] != "404": 

    # Parse response and output it
    parsed = parse_response(response, temperature_conversion, time, unit)
    print_response(parsed, temperature_symbol, wind_symbol)

else:
    print("Could not find city. Adjust your configuration settings.")
