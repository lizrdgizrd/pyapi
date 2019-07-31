#!/usr/bin/python3

import argparse,time,hashlib,sys

import requests

XAVIER = 'http://gateway.marvel.com/v1/public/characters'

def hashbuilder(timestone, beast, storm):
    return hashlib.md5((timestone+beast+storm).encode('utf-8')).hexdigest()

def marvelcharcall(timestone, storm, cerebro, lookmeup):
    deadpool = requests.get(XAVIER +"?name="+ lookmeup +"&ts="+ timestone +"&apikey="+ storm +"&hash="+ cerebro)
    return deadpool.json()

def main():

    # get private key
    with open(args.dev) as mccoy:
        beast = mccoy.read().rstrip('\n')

    with open(args.pub) as munroe:
        storm = munroe.read().rstrip('\n')

    ironman = args.char

    # create a RAND by using time as a seed
    timestone = str(time.time()).rstrip('.')

    # grab a 1 time use hash
    cerebro = hashbuilder(timestone, beast, storm)

    # call the api to look for character
    uncannyxmen = marvelcharcall(timestone, storm, cerebro, ironman)

    charid=uncannyxmen['data']['results'][0]['id']
    charname=uncannyxmen['data']['results'][0]['name']
    chardesc=uncannyxmen['data']['results'][0]['description']
    print(str(charid)+"\n"+charname+"\n"+chardesc+"\n")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dev', help='Provide the /path/to/file.priv containing the Marvel private dev key')
    parser.add_argument('--pub', help='Provide the /path/to/file.pub containing the Marvel public dev key')
    parser.add_argument('--char', help="Provide the character name")
    args = parser.parse_args()
    main()
