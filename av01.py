#!/usr/bin/python3

import requests, sqlite3

URI = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=S&datatype=json&apikey="

conn = sqlite3.connect('stock.db')

def main():

    addop = '''INSERT INTO SPRINT (DATE,OPEN,HIGH,LOW,CLOSE,VOLUME) VALUES('''
    
    try:
        conn.execute('''CREATE TABLE SPRINT
            (DATE TEXT PRIMARY KEY NOT NULL,
            OPEN REAL, HIGH REAL, LOW REAL,
            CLOSE REAL, VOLUME REAL);''')
    except Exception as err:
        print("DB creation error: "+err)
    
    try:
        with open("alphavantage.key","r") as avkey:
            newURI = URI + avkey.read()
    except Exception as err:
        print("Error opening file: "+str(err))

    theData = requests.get(newURI).json()

    theDaily = theData["Time Series (Daily)"]
    for x in theDaily:
        theDay = "'"+x+"'"
        for y in theDaily[x]:
            theDay += ", "+theDaily[x][y]
        theDay += ' )'
        #print(addop + theDay)

        try:
            conn.execute(addop + theDay)
        except Exception as err:
            print("Error writing to DB: " + str(err))
        else:     
            conn.commit()

    conn.close()
    

#    for x in theDaily:
#        print(x[])

main()
