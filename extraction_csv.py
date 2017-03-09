import csv
import sqlite3

conn = sqlite3.connect('fichierDonnees')
cur = conn.cursor()

file = open("res/23440003400026_J335_installations_table.csv","r")
test = csv.reader(file)
for row in test:
    numero=int(row[1])
    nom=row[0]
    ville=row[2]
    latitude=float(row[10])
    longitude=float(row[9])
    adresse=(row[5]+''+row[6]+''+row[7])
    if row[4]!='' :
        cp=int(row[4])
    """cur.execute("INSERT INTO Installation(numero,nom,ville,latitude,longitude,adresse,code_postal) VALUES(?,?,?,?,?,?,?);", (numero,nom,ville,latitude,longitude,adresse,cp))"""

file = open("res/J334_equipements_activites.csv","r")
test = csv.reader(file)

tmp1=0
tmp2=0
for row in test:
    if row[4]!='' :
        code=int(row[4])
    nom=row[5]
    equipementId=int(row[2])
    """if cur.execute("SELECT code, equipementId FROM Activité WHERE code = ? and equipementId = ?;", (code,equipementId, ))==None:"""
    cur.execute("SELECT * FROM Activité WHERE code = ? and equipementId = ?;", (code,equipementId))
    rows = cur.fetchall();
    for row in rows:
        print(row)
    cur.execute("INSERT INTO Activité(code,nom,equipementId) VALUES(?,?,?);", (code,nom,equipementId))
    """if tmp1==0 and tmp2==0 :
        cur.execute("INSERT INTO Activité(code,nom,equipementId) VALUES(?,?,?);", (code,nom,equipementId))
    elif tmp1!=code and tmp2!=equipementId :
        cur.execute("INSERT INTO Activité(code,nom,equipementId) VALUES(?,?,?);", (code,nom,equipementId))
    cur.execute("SELECT * from Activité;")
    rows = cur.fetchall();
    print(str(code)+' '+str(equipementId))
    for row in rows:
        tmp1 = row[0]
        tmp2 = row[2]"""

file = open("res/equipements.csv","r")
test = csv.reader(file)
for row in test:
    id=int(row[4])
    nom=row[3]
    InsNumeroInstall=int(row[2])
    """cur.execute("INSERT INTO Equipement(id,nom,InsNumeroInstall) VALUES(?,?,?);", (id,nom,InsNumeroInstall))"""

conn.commit()
cur.close()
conn.close()
