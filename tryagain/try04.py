#!/usr/bin/python3

import uuid

#simulate a job number with uuid package
ticket = uuid.uuid1()

try:
    print("Please enter config file to load")
    configfile = input("Filename: ")
    with open(configfile, 'r') as configfileobj:
        switchconfig = configfileobj.read()
except:
    x = "Error obtaining config file infomation"
else:
    x = "Switch file found"
finally:
    with open("try04.log", 'a') as zlog:
        print("\nWriting results of service to log file")
        print(ticket, " - ", x, file=zlog)
