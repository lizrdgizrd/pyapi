#!/usr/bin/python3

from flask import Flask
from flask import render_template
import requests

app = Flask(__name__)

URI = "https://www.anapioficeandfire.com/api/houses?pagesize=25"

def getHouses():
    ice = requests.get(URI)
    return ice.json()

@app.route("/houses")
def list_houses():
    got = getHouses()
    HouseList = [{"house":"House Name", "words":"House Motto"}]
    for x in got:
        name = x['name']
        HouseList.append({"house":name, "words":x['words']})
    
    return render_template("ASOIFhouses.html", houses = HouseList) 
        
if __name__ == "__main__":
    app.run(port=5006)

