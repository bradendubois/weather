from unit_conversions import temperature_conversion, wind_direction_conversion, wind_speed_conversion

def parse_response(api_response: dict):

    main = api_response["main"]
    wind = api_response["wind"]

    response = {
        "temperature": temperature_conversion(main["temp"]),
        "feels_like": temperature_conversion(main["feels_like"]),
        "minimum": temperature_conversion(main["temp_min"]),
        "maximum": temperature_conversion(main["temp_max"]),
        "humidity": main["humidity"],
        "wind_speed": wind_speed_conversion(wind["speed"]),
        "gusts": wind_speed_conversion(wind["gust"]),
        "direction": wind_direction_conversion(wind["deg"]),
        "name": api_response["name"],
        "description": api_response["weather"][0]["description"]
    }

    return response
