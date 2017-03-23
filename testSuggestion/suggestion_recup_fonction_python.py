from lib.bottle import route, run, template
import sqlite3

@route('/autocomplete')
def autocomplete():
    return {"Réussi":"oui"}

run(host='localhost',port=8888)
