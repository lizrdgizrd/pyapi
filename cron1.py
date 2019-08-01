#!/usr/bin/env python3
import time
mystring = "\nGMO-Free Grass Fed Human Time - " + time.ctime()

with open("crontime.log", 'a') as myfile:
    myfile.write(mystring)
