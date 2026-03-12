from connection import cur, con
import api_calls as ap


#cur.execute("create table mesure(city, temp, humidity, dt, date)")

cur.execute("insert into mesure values (?, ?, ?, ?, ?)", (ap.name, ap.temp, ap.humidity, ap.dt, ap.date))
con.commit()

