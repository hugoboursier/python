import http.client
from urllib.parse import urlencode
import json

API_KEY = "AIzaSyC4EPbSZDEf-p3ATdkewfw0nVsETDeD5dQ"

try:
    location = input('Entrez une adresse : ')
    conn = http.client.HTTPConnection("www.python.org")
    conn.request("GET", "/index.html")
    r1 = conn.getresponse()
    print(r1.status, r1.reason)

    urlParams = {'location': location, 'key': API_KEY, 'inFormat':'kvp', 'outFormat':'json'}
    url = "/geocoding/v1/address?" + urlencode(urlParams)
    conn = http.client.HTTPConnection("www.mapquestapi.com")

    conn.request("GET", url)
    print(conn.getresponse())

    res = conn.getresponse()
    print(res.status, res.reason)
    data = res.read()
    jsonData = json.loads(data)
    # FIXME le print n'est pas très secure...
    print(jsonData['results'][0]['locations'][0]['latLng'])
except Exception as err:
    print("Unexpected error: {0}".format(err))
finally:
    conn.close()
