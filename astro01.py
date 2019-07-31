#!/usr/bin/python3

import requests

ASTRO = "http://api.open-notify.org/astros.json"

try:
    astrolist = requests.get(ASTRO).json()
except:
    print("Can't make the request")


with open('astrofile.txt', 'a') as names:
    for x in astrolist['people']:
        names.write(x['name']+"\n")

print(astrolist)
