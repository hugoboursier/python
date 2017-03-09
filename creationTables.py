import sqlite3

fichierDonnees ="/hometu/etudiants/d/e/E154890J/Bureau/Python/python/db.sq3"
conn = sqlite3.connect('fichierDonnees')
cur = conn.cursor()
"""
cur.execute("drop table Installation")
cur.execute("drop table Equipement")
cur.execute("drop table Activité")
cur.execute("drop table Equip_Act")
"""

cur.execute("CREATE TABLE IF NOT EXISTS Installation (numero INTEGER PRIMARY KEY, nom TEXT, ville TEXT, latitude REAL, longitude REAL, adresse TEXT, code_postal INTEGER)")
cur.execute("CREATE TABLE IF NOT EXISTS Equipement (id INTEGER PRIMARY KEY, nom TEXT, insNumeroInstall INTEGER,FOREIGN KEY(insNumeroInstall) REFERENCES Installation(numero))")
cur.execute("CREATE TABLE IF NOT EXISTS Activité (code INTEGER, nom TEXT, equipementId INTEGER,FOREIGN KEY(equipementId) REFERENCES Equipement(id),PRIMARY KEY(code,equipementId))")

conn.commit()
cur.close()
conn.close()
