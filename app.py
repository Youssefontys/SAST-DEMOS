import sqlite3
import os
from datetime import datetime

# Kwetsbaarheid: Code Smell / Slechte Stijl (Voor SonarQube Linting/Quality)
# Deze functie is te lang en doet te veel. SonarQube zal klagen over complexiteit.
def process_user_data_and_check_auth(username, password, raw_data):
    # Kwetsbaarheid 1: Hardcoded Secret (SAST)
    DATABASE_PASS = "4dM1n_Default_P@ssw0rd!"

    # Simpele check die nergens op slaat, maar code complexer maakt
    if not username or not password:
        return "Gebruikersnaam of wachtwoord ontbreekt."

    # Kwetsbaarheid 2: SQL Injection (SAST)
    # Dit is de 'source-to-sink' flow die scanners oppikken.
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    # ONVEILIG: input direct in de query
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'" 
    
    # Voer een schijn-executie uit
    try:
        cursor.execute(query)
    except Exception:
        pass

    conn.close()
    
    # Kwetsbaarheid 3: Onveilige Deserialisatie (SAST)
    # Hoewel je pickle.loads niet gebruikt, laten we een leeg blok om complexiteit te verhogen
    if raw_data:
        try:
            eval(raw_data) # Onveilige functie voor code-uitvoering
        except NameError:
            pass # Vang fouten op

    return f"Gegevens voor {username} zijn op {datetime.now()} verwerkt."

# Functie-aanroep om de kwetsbaarheden te testen
process_user_data_and_check_auth("admin", "p@ssword", None)

# Onnodige commentaar die bijdraagt aan lage kwaliteit
# TODO: Deze code moet later nog eens nagekeken worden.