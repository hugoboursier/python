import sqlite3
"""Connexion a la base de données"""
fichierDonnees ="/hometu/etudiants/d/e/E154890J/Bureau/Python/python/db.sq3"
conn = sqlite3.connect('fichierDonnees')
cur = conn.cursor()


"""Suppresion des tables si elles existe déjà"""
"""
cur.execute("drop table Installation")
cur.execute("drop table Equipement")
cur.execute("drop table Activité")
cur.execute("drop table Equip_Act")
"""

"""Création des tables si la table n'existe pas avec les différentes conditions(primary key, foreigne key...)"""
cur.execute("CREATE TABLE IF NOT EXISTS Installation (numero INTEGER PRIMARY KEY, nom TEXT, ville TEXT, latitude REAL, longitude REAL, adresse TEXT, code_postal INTEGER)")
cur.execute("CREATE TABLE IF NOT EXISTS Equipement (id INTEGER PRIMARY KEY, nom TEXT, insNumeroInstall INTEGER,FOREIGN KEY(insNumeroInstall) REFERENCES Installation(numero))")
cur.execute("CREATE TABLE IF NOT EXISTS Activité (code INTEGER, nom TEXT, equipementId INTEGER,FOREIGN KEY(equipementId) REFERENCES Equipement(id),PRIMARY KEY(code,equipementId))")

conn.commit()
cur.close()
conn.close()
