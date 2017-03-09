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

cur.execute("CREATE TABLE Installation (numero INTEGER PRIMARY KEY, nom TEXT, ville TEXT, latitude REAL, longitude REAL, adresse TEXT, code_postal INTEGER)")
cur.execute("CREATE TABLE Equipement (id INTEGER PRIMARY KEY, nom TEXT, insNumeroInstall INTEGER,FOREIGN KEY(insNumeroInstall) REFERENCES Installation(numero))")
cur.execute("CREATE TABLE Activité (code INTEGER, nom TEXT, equipementId INTEGER,FOREIGN KEY(equipementId) REFERENCES Equipement(id),PRIMARY KEY(code,equipementId))")

cur.execute("CREATE TABLE Equip_Act(idEquip INTEGER,codeAct INTEGER,PRIMARY KEY(idEquip,codeAct))")

conn.commit()
cur.close()
conn.close()
