#!/usr/bin/env python

import json 
import requests

from util.parse_response import parse_response
from util.print_response import print_response

# Load the config file
with open("config.json") as f:
    data = json.load(f)

# API Key / City for query
api_key = data["api_key"]
city = data["city"]

# Settings haven't been configured
if api_key == "API_KEY_HERE" or city == "CITY_HERE":
    print("Config file not fully set up.")
    exit(-1)

# URL to query the openweathermap API
url = "http://api.openweathermap.org/data/2.5/weather?appid={}&q={}".format(api_key, city)

# Make request, parse result
response = requests.get(url).json()

# 404 === location not found
if response["cod"] != "404": 

    # Parse response and output it
    parsed = parse_response(response)
    print_response(parsed)

else:
    print("Could not find city. Adjust your configuration settings.")