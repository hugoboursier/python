# coding: utf-8
from bottle import route, run, template
import sqlite3
import json

"""Fonction de l'api qui cherche les installations sportives pour une ville donnée"""
@route('/ville/<name>')
def index(name):
    """Connexion à la base de données"""
    conn = sqlite3.connect('fichierDonnees')
    cur = conn.cursor()
    """Recherche dans la base de données les installations sportives pour la ville entrée en paramètre"""
    cur.execute("SELECT nom FROM Installation WHERE ville = ?;", (name, ))
    rows = cur.fetchall()
    """On ajoute les installations sportives dans un fichier au format json qu'on retourne par la suite"""
    lst = []
    for row in rows:
        d = {}
        d['Installation']=row[0]
        lst.append(d)
    return json.dumps(lst)



"""Fonction de l'api qui cherche les installations sportives et les villes où elles sont situées pour un sport donné"""
@route('/activite/<name>')
def index(name):
    """Connexion à la base de données"""
    conn = sqlite3.connect('fichierDonnees')
    cur = conn.cursor()
    """Recherche dans la base de données les installations sportives et les villes où elles sont situées pour un sport passé en paramètre"""
    cur.execute("SELECT DISTINCT i.nom, i.ville FROM Installation i,Equipement e,Activité a WHERE i.numero=e.insNumeroInstall and e.id=a.equipementId and a.nom=?", (name, ))
    rows = cur.fetchall()
    lst = []
    """On ajoute les installations sportives et les villes dans un fichier au format json qu'on retourne par la suite"""
    for row in rows:
        d = {}
        d['Installation']=row[0]
        d['ville']=row[1]
        lst.append(d)
    return json.dumps(lst)


"""Fonction de l'api qui cherche toutes les villes de la base de données pour la fonction d'autocomplete"""
@route('/recupVilles')
def index():
    """Connexion à la base de données"""
    conn = sqlite3.connect('fichierDonnees')
    cur = conn.cursor()
    """Recherche de toute les villes dans la base de données"""
    cur.execute("SELECT DISTINCT i.ville FROM Installation i")
    rows = cur.fetchall()
    communes = []
    """On ajoute les villes dans un fichier json qu'on retourne par la suite"""
    for row in rows:
        commune = {}
        commune['Nom'] = row[0]
        communes.append(commune)
    return json.dumps(communes)


"""Fonction de l'api qui cherche toutes les activités de la base de données pour la fonction d'autocomplete"""
@route('/recupActivites')
def index():
    """Connexion à la base de données"""
    conn = sqlite3.connect('fichierDonnees')
    cur = conn.cursor()
    """Recherche de toute les activités dans la base de données"""
    cur.execute("SELECT DISTINCT a.nom FROM Activité a")
    rows = cur.fetchall()
    activites = []
    """On ajoute les activités dans un fichier json qu'on retourne par la suite"""
    for row in rows:
        activite = {}
        activite['Nom'] = row[0]
        activites.append(activite)
    return json.dumps(activites)

"""@route('/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./public')
"""
run(host='localhost', port=8888)
