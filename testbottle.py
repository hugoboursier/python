# coding: utf-8
from bottle import route, run, template
import sqlite3
import json

@route('/ville/<name>')
def index(name):
    conn = sqlite3.connect('fichierDonnees')
    cur = conn.cursor()
    cur.execute("SELECT nom FROM Installation WHERE ville = ?;", (name, ))
    rows = cur.fetchall()
    lst = []
    for row in rows:
        d = {}
        d['Installation']=row[0]
        lst.append(d)
    return json.dumps(lst)

@route('/activite/<name>')
def index(name):
    conn = sqlite3.connect('fichierDonnees')
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT i.nom, i.ville FROM Installation i,Equipement e,Activité a WHERE i.numero=e.insNumeroInstall and e.id=a.equipementId and a.nom=?", (name, ))
    rows = cur.fetchall()
    lst = []
    for row in rows:
        d = {}
        d['Installation']=row[0]
        d['ville']=row[1]
        lst.append(d)
    return json.dumps(lst)

@route('/recupVilles/<nomVille>')
def index(nomVilles):
    conn = sqlite3.connect('fichierDonnees')
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT i.ville FROM Installation i where i.ville = ?",(nomVilles,))
    rows = cur.fetchall()
    communes = []
    for row in rows:
        commune = {}
        commune['Nom'] = row[0]
        communes.append(commune)
    return json.dumps(communes)

@route('/recupActivites/<nomAct>')
def index(nomAct):
    conn = sqlite3.connect('fichierDonnees')
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT a.nom FROM Activité a where a.nom =?",(nomAct,))
    rows = cur.fetchall()
    activites = []
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
