from lib.bottle import route, run, template
import sqlite3


@route('/ville/<name>')
def index(name):
    conn = sqlite3.connect('fichierDonnees')
    cur = conn.cursor()
    cur.execute("SELECT nom FROM Installation WHERE ville = ?;", (name, ))
    rows = cur.fetchall()
    stre = ""
    for row in rows:
        stre = stre + str(row) + "<br>"

    return stre

@route('/activite/<name>')
def index(name):
    conn = sqlite3.connect('fichierDonnees')
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT i.nom, i.ville FROM Installation i,Equipement e,Activité a WHERE i.numero=e.insNumeroInstall and e.id=a.equipementId and a.nom=?", (name, ))
    rows = cur.fetchall()
    stre = ""
    for row in rows:
        stre = stre + str(row) + "<br>"
    return stre

run(host='localhost', port=8888)
