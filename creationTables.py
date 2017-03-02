import sqlite3

fichierDonnees ="/hometu/etudiants/b/o/E155590U/2eme_annee/python/python/db.sq3"
conn = sqlite3.connect('fichierDonnees')
cur = conn.cursor()
cur.execute("CREATE TABLE Installation (numero INTEGER, nom TEXT, ville TEXT, latitude REAL, longitude REAL, adresse TEXT, code_postal INTEGER)")
cur.execute("CREATE TABLE Equipement (id INTEGER, nom TEXT, InsNumeroInstall INTEGER)")
cur.execute("CREATE TABLE Activité (code INTEGER, nom TEXT, equipementId INTEGER)")
conn.commit()
cur.close()
conn.close()
