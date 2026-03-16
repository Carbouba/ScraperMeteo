import sqlite3

# Connexion a la base SQLite.
# Note: le fichier `.db` sera cree automatiquement s'il n'existe pas.
# Ici, le nom du fichier est "wheather_data.db".
con = sqlite3.connect("wheather_data.db")

# Cursor reutilisable pour executer des requetes (SELECT/INSERT/CREATE TABLE...).
cur = con.cursor()
