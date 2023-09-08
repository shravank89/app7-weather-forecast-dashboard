import requests

API_KEY = "640037a527588ff6ab64d7c40ea2d084"


def get_data(place, days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    if response.json()["message"] == 0:
        content = response.json()["list"][:8*days]
        return content
    else:
        return response.json()["message"]

