import csv
import sqlite3

conn = sqlite3.connect('fichierDonnees')
cur = conn.cursor()

file = open("res/23440003400026_J335_installations_table.csv","r")
test = csv.reader(file)
for row in test:
    numero=row[1]
    nom=row[0]
    ville=row[2]
    latitude=row[10]
    longitude=row[9]
    adresse=(row[5]+''+row[6]+''+row[7])
    cp=row[4]
    cur.execute("INSERT INTO Installation(numero,nom,ville,latitude,longitude,adresse,code_postal) VALUES(?,?,?,?,?,?,?);", (numero,nom,ville,latitude,longitude,adresse,cp))

file = open("res/J334_equipements_activites.csv","r")
test = csv.reader(file)
for row in test:
    code=row[4]
    nom=row[5]
    equipementId=row[2]
    cur.execute("INSERT INTO Activité(code,nom,equipementId) VALUES(?,?,?);", (code,nom,equipementId))

file = open("res/equipements.csv","r")
test = csv.reader(file)
for row in test:
    id=row[4]
    nom=row[3]
    InsNumeroInstall=row[2]
    cur.execute("INSERT INTO Equipement(id,nom,InsNumeroInstall) VALUES(?,?,?);", (id,nom,InsNumeroInstall))

conn.commit()
cur.close()
conn.close()
