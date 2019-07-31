#!/usr/bin/python3

import requests

URI = "https://www.anapioficeandfire.com/api/houses?pagesize=25"

def getHouses():
    ice = requests.get(URI)
    return ice.json()

def main():
    got = getHouses()
    for x in got:
        name = x['name']
        if len(name)<=14:
            name += "\t\t"
        print(name+'\t'+x['words']) 

main()
