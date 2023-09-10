def DoLoad():
    import datetime
    import coordinates
    import requests
    import json



    data = coordinates.Get_Coordinates()
    latitude = data[0]
    longitude = data[1]
    city = data[2]

    WEATHER_API_KEY = ''

    CURRENT_WEATHER_API_CALL = (
            'https://api.openweathermap.org/data/2.5/weather?'
            f'lat={latitude}&lon={longitude}&'
            'appid=' + WEATHER_API_KEY + '&units=metric'
    )

    response = requests.get(CURRENT_WEATHER_API_CALL)
    sunriseDate = response.json()['sys']['sunrise']
    sunsetDate = response.json()['sys']['sunset']

    with open("data/sunrise.txt", "w+") as sunrise_file:
        sunrise_file.write(str(sunriseDate))
        sunrise_file.close()

    with open("data/sunset.txt", "w+") as sunset_file:
        sunset_file.write(str(sunsetDate))
        sunset_file.close()

    with open("data/city.txt", "w+") as city_file:
        city_file.write(city)
        city_file.close()