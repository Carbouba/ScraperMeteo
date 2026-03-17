import sys
from connection import cur, con
from api_calls import get_weather, get_coordinates
from config import API_KEY

# Ce fichier regroupe les requetes SQL sur SQLite (lecture + insertion).
# Il s'appuie sur:
# - `connection.py` pour la connexion/cursor (cur, con)
# - `api_calls.py` pour recuperer une mesure meteo depuis OpenWeatherMap
# - `config.py` pour la cle API (API_KEY)

def get_temp_date():
    # Recupere deux listes paralleles: temperatures et dates, triees par date.
    cur.execute("select temp, date from mesure order by date")
    res = cur.fetchall()

    list_temp = []
    list_date = []

    # `res` contient des tuples du type: (temp, date)
    for elements in res:
        temp = elements[0]
        date = elements[1]
        list_temp.append(temp)
        list_date.append(date)

    # Structure retournee: [ [temp1, temp2, ...], [date1, date2, ...] ]
    all_list = [list_temp, list_date]

    return all_list

def get_insert_data():
    # Recupere la meteo courante, puis insere en base si elle n'existe pas deja.
    coordonnee = get_coordinates("Paris", API_KEY)

    # `get_coordinates` renvoie [lat, lon]
    l_at = coordonnee[0]
    l_on = coordonnee[1]

    Current_Weather = get_weather(l_at, l_on, API_KEY)

    # `get_weather` renvoie [city, temp, humidity, dt, date]
    name = Current_Weather[0]
    temp = Current_Weather[1]
    humidity = Current_Weather[2]
    dt = Current_Weather[3]
    date = Current_Weather[4]
    wind = Current_Weather[5]

    # Cree la table si elle n'existe pas encore.
    # (Le schema est simple: city, temp, humidity, dt, date)
    #cur.execute("CREATE TABLE IF NOT EXISTS mesure(id INTEGER PRIMARY KEY AUTOINCREMENT, city, temp, humidity, dt, date, wind)")

    #Ajouter une colonne
    #cur.execute("alter table mesure add column wind")

    # Suppression d'une ligne avec id = 5
    #cur.execute("DELETE FROM mesure ")

    # Deduplication: on verifie si on a deja une ligne pour ce timestamp `dt`.
    cur.execute("select * from mesure where dt = ?", (dt,))
    res = cur.fetchall()

    if res:
        # Si une ligne existe deja, on ne reinserre pas.
        pass
    else:
        # Sinon on insere et on commit.
        cur.execute("""INSERT INTO mesure (city, temp, humidity, dt, date, wind)
                     VALUES (?, ?, ?, ?, ?, ?)""", 
                     (name, temp, humidity, dt, date, wind))
        con.commit()


get_insert_data()




