import http.client
from urllib.parse import urlencode
import json

API_KEY = "AIzaSyC4EPbSZDEf-p3ATdkewfw0nVsETDeD5dQ"

try:
    conn = HTTPSConnection("localhost",3128)
    conn.set_tunnel("www.example.com",443)
    conn.send('...etc...')

    """
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
    print(jsonData['results'][0]['locations'][0]['latLng'])"""
except Exception as err:
    print("Unexpected error: {0}".format(err))
finally:
    conn.close()
