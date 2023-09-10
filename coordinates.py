from urllib.request import urlopen
from dataclasses import dataclass
import json



@dataclass(slots=True, frozen=True)
class Coordinates:
    latitude: float
    longitude: float
    city: str


def Get_Coordinates() -> Coordinates:
    data = Get_IpData()
    latitude = data['loc'].split(',')[0]
    longitude = data['loc'].split(',')[1]
    city = data['city'].split(',')[0]

    result = list()
    result.append(latitude)
    result.append(longitude)
    result.append(city)
    return result


def Get_IpData() -> dict:
    url = 'http://ipinfo.io/json'
    response = urlopen(url)
    return json.load(response)