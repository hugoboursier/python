import sqlite3

fichierDonnees ="/hometu/etudiants/b/o/E155590U/2eme_annee/python/python/db.sq3"
conn = sqlite3.connect('fichierDonnees')
cur = conn.cursor()
"""
cur.execute("INSERT INTO membres(age,nom,taille) VALUES(21,'Dupont',1.83)")
cur.execute("INSERT INTO membres(age,nom,taille) VALUES(15,'Blumâr',1.57)")
cur.execute("INSERT Into membres(age,nom,taille) VALUES(18,'Özémir',1.69)")
"""
conn.commit()
cur.close()
conn.close()

