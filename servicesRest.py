import sqlite3


"""Fichier qui servait à essayer les différentes fonctions qui seront dans l'API"""


"""Connexion à la base de données"""
conn = sqlite3.connect('fichierDonnees')
cur = conn.cursor()


"""Fonction qui cherche les installations sportives pour une ville donnée"""
def rechercheVille(ville):
    cur.execute("SELECT nom FROM Installation WHERE ville = ?;", (ville, ))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    if(len(rows)==0):
        return False
    else :
        return True
"""rechercheVille("Nantes")"""

"""Fonction qui cherche les installations sportives donnée"""
def rechercheActivite(activite):
    cur.execute("SELECT DISTINCT i.nom, i.ville FROM Installation i,Equipement e,Activité a WHERE i.numero=e.insNumeroInstall and e.id=a.equipementId and a.nom=?", (activite, ))
    rows = cur.fetchall()

    for row in rows:
        print(row)
        
    if(len(rows)==0):
        return False
    else :
        return True
"""rechercheActivite("Basket-Ball")"""
