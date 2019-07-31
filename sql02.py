#!/usr/bin/python3

import sqlite3

try:
    conn = sqlite3.connect('test.db')
except Exception as err:
    print("Error opening DB: "+ str(err))
else:
    print ("Opened DB successfully")

    addop = '''INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES('''
    success = True

    try:
        conn.execute(addop+ "1, 'Paul', 32, 'California', 20000.00 )")
    except Exception as err:
        print("Error adding record: "+str(err))
        success=False

    try:
        conn.execute(addop+ "2, 'Allen', 25, 'Texas', 15000.00 )")
    except Exception as err:
        print("Error adding record: "+str(err))
        succcess=False

    try:
        conn.execute(addop+ "3, 'Teddy', 23, 'Norway', 20000.00 )")
    except Exception as err:
        print("Error adding record: "+str(err))
        success=False

    try:
        conn.execute(addop+ "4, 'Mark', 25, 'Rich-Mond ', 65000.00 )")
    except Exception as err:
        print("Error adding record: "+str(err))
        success=False

if(success):   
    conn.commit()
    print("Records created successfully")


rec = conn.execute("SELECT * FROM COMPANY")
for row in rec:
    print(row)

conn.close()
