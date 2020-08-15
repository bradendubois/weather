<div>
  <img align="left" width="150px" src="icon.png" alt="Sun icon" />
  <h1 margin="auto">weather</h1>
</div>

A quick weather-check using the [OpenWeatherMap API](https://openweathermap.org/).

<br />

## Requirements

- [Python 3](https://www.python.org/)
- An **API Key** from [OpenWeatherMap](https://openweathermap.org/api) (a free option is available)

## Installation / Setup

First, clone the project:

```shell_script
git clone https://github.com/bradendubois/weather
cd weather
```

Open the ``configuration.json`` file and fill in your settings.

```json
{
    "api_key": "API_KEY_HERE",
    "city": "CITY_HERE",
    "temperature_unit": "celsius|fahrenheit|kelvin",
    "wind_unit": "m|f|km|miles / second|minute|h"  
}
```

- ``api_key``: the key obtained from [OpenWeatherMap](https://openweathermap.org/)
- ``city``: the location to query. Verify that it is supported by searching in [OpenWeatherMap](https://openweathermap.org/)
- ``temperature_unit``: whichever unit to rely on, Celsius, Fahrenheit, or Kelvin.
- ``wind_unit``: what distance/time units to present the result in. 
    - **distance**: metres, feet, kilometres, or miles
    - **time**: seconds, minutes, or hours

## Usage

Simply run the script:

```shell_script
./weather.py
```

Or in Python:

```shell_script
python weather.py
```

A summary of the weather will be printed.

#### Example

```
> python weather.py

    Currently, in Saskatoon:
    Few clouds
    Temperature: 13.9°C (feels like: 10.9°C)
    High: 15°C, Low: 13°C
    Wind (SW) speeds of 11.2km/h
    Humidity: 62%
```

## Acknowledgements

- The sun icon used in this README is provided by [Max Pixel](https://www.maxpixel.net/Icon-Climate-Sky-Summer-Sun-Sunny-Weather-2947294), licensed by [CC0](https://creativecommons.org/publicdomain/zero/1.0/deed.en). 
- [OpenWeatherMap](https://openweathermap.org/) provides a great, easy to use API for obtaining weather information, all for free.
