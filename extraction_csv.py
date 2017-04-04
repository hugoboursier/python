import csv
import sqlite3

"""Connexion à la base de données"""
conn = sqlite3.connect('fichierDonnees')
cur = conn.cursor()

"""Récupération du fichier csv à extraire"""
file = open("res/23440003400026_J335_installations_table.csv","r")
test = csv.reader(file)
"""Récupération des données choisies à ajouter à la base de données"""
for row in test:
    numero=int(row[1])
    nom=row[0]
    ville=row[2]
    latitude=float(row[10])
    longitude=float(row[9])
    adresse=(row[5]+''+row[6]+''+row[7])
    """On cast le code postal en int afin qu'il soit en adéquation avec les conditions de la base de données"""
    if row[4]!='' :
        cp=int(row[4])
    cur.execute("INSERT INTO Installation(numero,nom,ville,latitude,longitude,adresse,code_postal) VALUES(?,?,?,?,?,?,?);", (numero,nom,ville,latitude,longitude,adresse,cp))



"""Récupération du fichier csv à extraire"""
file = open("res/J334_equipements_activites.csv","r")
test = csv.reader(file)
"""Récupération des données choisies à ajouter à la base de données"""
for row in test:
    """On cast le code postal en int afin qu'il soit en adéquation avec les conditions de la base de données"""
    if row[4]!='' :
        code=int(row[4])
    nom=row[5]
    """On cast l'identifiant de l'équipement en int afin qu'il soit en adéquation avec les conditions de la base de données"""
    equipementId=int(row[2])

    """On fait un select afin de savoir si la ligne à ajoutée est déjà dans la base de données"""
    cur.execute("SELECT * FROM Activité WHERE code = ? and equipementId = ?;", (code,equipementId))
    rows = cur.fetchall()

    """Si la longueur de rows est 0 cela veut dire que la nouvelle ligne à ajouté n'est pas dans la base de données donc on l'ajoute
    à la base de données sinon on passe à la ligne suivante"""
    if(len(rows)==0) :
        cur.execute("INSERT INTO Activité(code,nom,equipementId) VALUES(?,?,?);", (code,nom,equipementId))



"""Récupération du fichier csv à extraire"""
file = open("res/equipements.csv","r")
test = csv.reader(file)
"""Récupération des données choisies à ajouter à la base de données"""
for row in test:
    """On cast l'identifiant en int afin qu'il soit en adéquation avec les conditions de la base de données"""
    id=int(row[4])
    nom=row[3]
    """On cast le numéro de l'installation en int afin qu'il soit en adéquation avec les conditions de la base de données"""
    InsNumeroInstall=int(row[2])
    cur.execute("INSERT INTO Equipement(id,nom,InsNumeroInstall) VALUES(?,?,?);", (id,nom,InsNumeroInstall))

conn.commit()
cur.close()
conn.close()
