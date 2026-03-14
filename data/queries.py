from connection import cur, con
from api_calls import get_weather, get_coordinates
from config import API_KEY

def get_temp_date():
    cur.execute("select temp, date from mesure order by date")
    res = cur.fetchall()

    list_temp = []
    list_date = []

    for elements in res:
        temp = elements[0]
        date = elements[1]
        list_temp.append(temp)
        list_date.append(date)

    all_list = [list_temp, list_date]

    return all_list


# coordonnee = get_coordinates("Niamey", API_KEY)

# l_at = coordonnee[0]
# l_on = coordonnee[1]

# Current_Weather = get_weather(l_at, l_on, API_KEY)

# name = Current_Weather[0]
# temp = Current_Weather[1]
# humidity = Current_Weather[2]
# dt = Current_Weather[3]
# date = Current_Weather[4]

# #cur.execute("create table mesure(city, temp, humidity, dt, date)")

# cur.execute("select * from mesure where dt = ?", (dt,))
# res = cur.fetchall()

# if res:
#     pass
# else:
#     cur.execute("insert into mesure values (?, ?, ?, ?, ?)", (name, temp, humidity, dt, date))
#     con.commit()

get_temp_date()









