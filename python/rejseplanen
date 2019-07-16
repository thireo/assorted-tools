#!usr/bin/python

import requests
import pprint
import json

response = requests.get('http://xmlopen.rejseplanen.dk/bin/rest.exe/departureBoard?id=008600605&format=json')
pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(response.json())
b = json.dumps(response.json())

bb = response.json()
#print(bb["DepartureBoard"]["Departure"][0].get("rtarr"))
for d in bb["DepartureBoard"]["Departure"]:
    print(d.get("rtarr"))
#print(b)
