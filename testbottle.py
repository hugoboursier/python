from lib.bottle import route, run, template
import json
import sqlite3


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




run(host='localhost', port=8888)
