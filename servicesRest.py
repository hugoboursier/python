import sqlite3

conn = sqlite3.connect('fichierDonnees')
cur = conn.cursor()

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
