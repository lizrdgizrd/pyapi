#!/usr/bin/python3

import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully")

try:
    conn.execute('''CREATE TABLE COMPANY
        (ID INT PRIMARY KEY NOT NULL,
        NAME TEXT NOT NULL,
        AGE INT NOT NULL,
        ADDRESS CHAR(50),
        SALARY REAL);''')
except Exception as err:
    print("Error: "+str(err))
else:
    print("Table created successfully")
finally:
    print("Closing database")
    conn.close()
