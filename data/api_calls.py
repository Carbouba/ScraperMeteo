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

coordonnee = get_coordinates("Niamey", "80f5b5a7a497ad5e33582eac39c79b68")

l_at = coordonnee[0]
l_on = coordonnee[1]

Current_Weather = get_weather(l_at, l_on, "80f5b5a7a497ad5e33582eac39c79b68")

name = Current_Weather[0]
temp = Current_Weather[1]
humidity = Current_Weather[2]
dt = Current_Weather[3]
date = Current_Weather[4]





