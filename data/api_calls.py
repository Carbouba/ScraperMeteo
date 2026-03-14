import requests
from datetime import datetime

def get_coordinates(city_name, api_key):
    # 1. définir l'url
    url = "http://api.openweathermap.org/geo/1.0/direct"

    # 2. définir les params (city_name et api_key à la place des valeurs fixes)
    params = {
    "q": city_name,      # le nom de la ville
    "limit": 1,
    "appid": api_key
}
    # 3. envoyer la requête
    reponse = requests.get(url, params=params)

    # 4. lire la réponse en json
    data = reponse.json()

    # 5. retourner data
    dico = data[0]
    lat = dico["lat"]
    lon = dico["lon"]

    coord = [lat, lon]
    
    return coord

def get_weather(lat, lon, api_key):
    url = "https://api.openweathermap.org/data/2.5/weather"

    # 2. définir les params (city_name et api_key à la place des valeurs fixes)
    params = {
    "lat": lat,      # le nom de la ville
    "lon": lon,
    "appid": api_key,
    "units": "metric"
}

    reponse = requests.get(url, params=params)

    data = reponse.json()

    
    name = data["name"]
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    dt = data["dt"]
    date = datetime.fromtimestamp(dt).strftime("%Y-%m-%d")

    mesure = [name, temp, humidity, dt, date]

    return mesure







