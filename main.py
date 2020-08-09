import json 
import requests

from parse_response import parse_response

# Load the config file
with open("config.json") as f:
    data = json.load(f)

# API Key 
api_key = data["api_key"]

# City
city = data["city"]

# URL to query the openweathermap API
url = "http://api.openweathermap.org/data/2.5/weather?appid={}&q={}".format(api_key, city)

# Make request, parse result
response = requests.get(url).json()

# 404 === location not found
if response["cod"] != "404": 

    # Parse response
    # for key in response:
    #    print(key, response[key])

    parsed = parse_response(response)

    print(parsed)
    # data = response["main"]

    # for key in data:
    #     print(key, data[key])

else:
    print(" City Not Found ")