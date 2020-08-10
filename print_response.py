from unit_conversions import temperature_symbol, wind_symbol

TOP_PADDING = 1
LEFT_PADDING = 3
BOTTOM_PADDING = 0

def print_response(parsed_response: dict):

    message = [
        "Currently, in {}:".format(parsed_response["name"]),
        "{}".format(parsed_response["description"][0].upper() + parsed_response["description"][1:]),
        "Temperature: {:.1f}°{} (feels like: {:.1f}°{})".format(parsed_response["temperature"], temperature_symbol, parsed_response["feels_like"], temperature_symbol),
        "High: {:.0f}°{}, Low: {:.0f}°{}".format(parsed_response["maximum"], temperature_symbol, parsed_response["minimum"], temperature_symbol),
        "Wind ({}) speeds of {:.1f}{}, gusts of {:.1f}{}".format(parsed_response["direction"], parsed_response["wind_speed"], wind_symbol, parsed_response["gusts"], wind_symbol),
        "Humidity: {:.0f}%".format(parsed_response["humidity"])
    ]

    print("\n" * TOP_PADDING, end="")
    for line in message:
        print(" " * LEFT_PADDING + line)
    print("\n" * BOTTOM_PADDING, end="")