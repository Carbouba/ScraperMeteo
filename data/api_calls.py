import requests
from datetime import datetime

# Ce fichier regroupe les appels HTTP vers l'API OpenWeatherMap:
# - Geo API (direct geocoding): convertir "nom de ville" -> (lat, lon)
# - Weather API: recuperer la meteo courante a partir de (lat, lon)

def get_coordinates(city_name, api_key):
    # Objectif: obtenir les coordonnees GPS (latitude/longitude) d'une ville.

    # 1. définir l'url
    url = "http://api.openweathermap.org/geo/1.0/direct"

    # 2. définir les params (city_name et api_key à la place des valeurs fixes)
    params = {
    "q": city_name,      # le nom de la ville
    "limit": 1,
    "appid": api_key
}
    # 3. envoyer la requête
    # requests.get(..., params=...) construit automatiquement l'URL avec ?q=...&appid=...
    reponse = requests.get(url, params=params)

    # 4. lire la réponse en json
    # La reponse est une liste: [{...}] si un resultat est trouve, ou [] sinon.
    data = reponse.json()

    # 5. retourner data
    # Ici on prend le premier resultat (index 0) car limit=1.
    dico = data[0]
    lat = dico["lat"]
    lon = dico["lon"]

    coord = [lat, lon]

    return coord

def get_weather(lat, lon, api_key):
    # Objectif: recuperer la meteo courante a partir des coordonnees (lat, lon).
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

    # Champs utiles dans la reponse JSON.
    name = data["name"]
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    dt = data["dt"]
    wind = data["wind"]["speed"]

    # Conversion du timestamp Unix (dt) en date lisible (YYYY-MM-DD).
    date = datetime.fromtimestamp(dt).strftime("%Y-%m-%d")

    # "mesure" est une liste dans un ordre fixe utilise par queries.py
    # (city, temp, humidity, dt, date).
    mesure = [name, temp, humidity, dt, date, wind]

    return mesure






