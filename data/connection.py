from CTkMessagebox import CTkMessagebox
import sqlite3
import os


base_dir  = os.path.dirname(__file__)

try:
    # Connexion a la base SQLite.
    # Note: le fichier `.db` sera cree automatiquement s'il n'existe pas.
    # Ici, le nom du fichier est "wheather_data.db".
    con = sqlite3.connect(os.path.join(base_dir, "wheather_data.db"))

    # Cursor reutilisable pour executer des requetes (SELECT/INSERT/CREATE TABLE...).
    cur = con.cursor()
except sqlite3.Error as er:
    CTkMessagebox(title="Erreur BDD", message=f"Erreur SQLite : {er}", icon="cancel")
